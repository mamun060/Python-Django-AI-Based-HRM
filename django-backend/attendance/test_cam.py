# import cv2

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("❌ Cannot access camera")
#         break

#     cv2.imshow('Webcam Test', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
from utils.face_recognition import recognize_faces
from yolov8_wrapper import load_yolo_model  # your wrapper
from facenet_wrapper import load_facenet_model  # your wrapper
from reference_loader import load_reference_embeddings
import torch
from django.conf import settings
import os

# Load models
yolo_model = load_yolo_model()
facenet_model = load_facenet_model()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
facenet_model.to(device)

# Load known face embeddings
reference_dir = os.path.join(settings.MEDIA_ROOT, 'attendance')
reference_embeddings = load_reference_embeddings(reference_dir, facenet_model)

# Store last seen names to avoid flooding
last_seen = {}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run YOLO detection
    results = yolo_model(frame_rgb)

    faces = recognize_faces(frame_rgb, results, facenet_model, reference_embeddings)

    for face in faces:
        name = face["name"]
        x1, y1, x2, y2 = face["box"]

        # Avoid too frequent re-recording
        now = datetime.now()
        if name != "Unknown":
            last_time = last_seen.get(name)
            if not last_time or (now - last_time).total_seconds() > 60:  # Allow 1 min gap
                last_seen[name] = now
                print(f"[+] Detected: {name}")

        # Draw box and name
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f"{name}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("Live Attendance", frame)

    # Exit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
