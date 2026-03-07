import os
from PIL import Image
import torch
from torchvision.transforms import ToTensor, Resize, Compose, RandomRotation, RandomResizedCrop, ColorJitter
from torch.nn.functional import cosine_similarity
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
from datetime import datetime
from attendance.models import AttendanceRecord
from attendance.utils import update_daily_summary

from torchvision.transforms import (
    Compose, Resize, ToTensor, RandomRotation,
    ColorJitter, RandomHorizontalFlip,
    RandomPerspective, RandomResizedCrop
)

resize = Resize((160, 160))
to_tensor = ToTensor()

# Stronger augmentation pipeline
augment = Compose([
    RandomRotation(degrees=30),
    RandomHorizontalFlip(p=0.5),
    RandomPerspective(distortion_scale=0.4, p=0.7),
    ColorJitter(brightness=0.3, contrast=0.3, saturation=0.2),
    RandomResizedCrop(size=160, scale=(0.85, 1.0)),
])


def load_reference_embeddings(reference_dir, facenet):
    reference_embeddings = {}

    for person_name in os.listdir(reference_dir):
        person_dir = os.path.join(reference_dir, person_name)
        if not os.path.isdir(person_dir):
            continue

        for file in os.listdir(person_dir):
            if file.endswith(".jpg") or file.endswith(".png"):
                img_path = os.path.join(person_dir, file)
                img = Image.open(img_path).convert('RGB')  # ✅ You forgot this line

                # Augment the image to make embedding more general
                for i in range(5):  
                    aug_img = augment(img)
                    tensor = to_tensor(resize(aug_img)).unsqueeze(0)
                    tensor = (tensor - 0.5) / 0.5
                    with torch.no_grad():
                        embedding = facenet(tensor)

                    if person_name in reference_embeddings:
                        reference_embeddings[person_name].append(embedding)
                    else:
                        reference_embeddings[person_name] = [embedding]

    return reference_embeddings

def recognize_faces(frame_rgb, results, facenet, reference_embeddings):
    detected_faces = []
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    for result in results:
        for box in result.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box[:4])
            if (x2 - x1) < 60 or (y2 - y1) < 60:
                continue

            pad = 20
            h, w, _ = frame_rgb.shape
            x1 = max(0, x1 - pad)
            y1 = max(0, y1 - pad)
            x2 = min(w, x2 + pad)
            y2 = min(h, y2 + pad)

            face_img = frame_rgb[y1:y2, x1:x2]
            pil_face = Image.fromarray(face_img)
            face_tensor = to_tensor(resize(pil_face)).unsqueeze(0)
            face_tensor = (face_tensor - 0.5) / 0.5
            face_tensor = face_tensor.to(device)

            with torch.no_grad():
                face_embedding = facenet(face_tensor)

            best_match = "Unknown"
            best_score = 0.0
            threshold = 0.70

            for name, embeddings in reference_embeddings.items():
                for ref_emb in embeddings:
                    sim = cosine_similarity(ref_emb, face_embedding).item()
                    if sim > best_score and sim > threshold:
                        best_score = sim
                        best_match = name

            # ✅ Save record and update summary
            if best_match != "Unknown":
                buffer = BytesIO()
                pil_face.save(buffer, format="JPEG")
                image_file = ContentFile(buffer.getvalue(), name=f"{best_match}_{datetime.now().strftime('%H%M%S')}.jpg")

                AttendanceRecord.objects.create(
                    name=best_match,
                    accuracy=round(best_score * 100, 2),
                    image=image_file
                )

                update_daily_summary(best_match)

            detected_faces.append({
                "name": best_match,
                "score": round(best_score * 100, 2),
                "box": [x1, y1, x2, y2],
                "face_image": face_img
            })

    return detected_faces

# def recognize_faces(frame_rgb, results, facenet, reference_embeddings):
#     detected_faces = []

#     for result in results:
#         for box in result.boxes.xyxy:
#             x1, y1, x2, y2 = map(int, box[:4])

#             # Optional: skip small faces (to avoid bad crops)
#             if (x2 - x1) < 60 or (y2 - y1) < 60:
#                 continue

#             # Add padding
#             pad = 20
#             h, w, _ = frame_rgb.shape
#             x1 = max(0, x1 - pad)
#             y1 = max(0, y1 - pad)
#             x2 = min(w, x2 + pad)
#             y2 = min(h, y2 + pad)

#             face_img = frame_rgb[y1:y2, x1:x2]
#             pil_face = Image.fromarray(face_img)
#             face_tensor = to_tensor(resize(pil_face)).unsqueeze(0)
#             face_tensor = (face_tensor - 0.5) / 0.5


#             device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#             with torch.no_grad():
#                 face_embedding = facenet(face_tensor.to(device))

#             best_match = "Unknown"
#             best_score = 0.0
#             threshold = 0.70  # Lowered for motion blur tolerance

#             for name, embeddings in reference_embeddings.items():
#                 for ref_emb in embeddings:
#                     sim = cosine_similarity(ref_emb, face_embedding).item()
#                     if sim > best_score and sim > threshold:
#                         best_score = sim
#                         best_match = name

#             detected_faces.append({
#                 "name": best_match,
#                 "score": round(best_score * 100, 2),
#                 "box": [x1, y1, x2, y2],
#                 "face_image": face_img
#             })

#     return detected_faces
