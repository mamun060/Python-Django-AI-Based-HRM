# import os
# import cv2
# import time
# import numpy as np
# from PIL import Image
# from datetime import timedelta
# from django.utils import timezone
# from django.core.files.base import ContentFile
# from django.conf import settings
# from .models import AttendanceRecord
# from .utils.model_loader import load_yolo_model, load_facenet_model
# from .utils.face_recognition import recognize_faces, load_reference_embeddings

# # Load models once
# yolo_model = load_yolo_model()
# facenet_model = load_facenet_model()

# # Load known face embeddings
# reference_dir = os.path.join(settings.BASE_DIR, 'data','media')
# reference_embeddings = load_reference_embeddings(reference_dir, facenet_model)

# def process_rtsp_stream():
#     rtsp_url = 'rtsp://nabi:demo12345@192.168.2.194:554/h264'
#     cap = cv2.VideoCapture(rtsp_url)

#     if not cap.isOpened():
#         print("[ERROR] Unable to open RTSP stream.")
#         return

#     print("[INFO] RTSP facial recognition started...")
#     print(f"[INFO] Loaded reference names: {list(reference_embeddings.keys())}")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("[WARNING] Frame read failed, retrying in 1 second...")
#             time.sleep(1)
#             continue

#         try:
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             results = yolo_model.predict(source=frame_rgb, conf=0.5, verbose=False)
#             print(f"[INFO] YOLO detected {len(results[0].boxes)} faces.")

#             detected_faces = recognize_faces(frame_rgb, results, facenet_model, reference_embeddings)

#             if not detected_faces:
#                 print("[INFO] No recognizable faces detected.")

#             for face in detected_faces:
#                 name = face["name"]
#                 score = face["score"]

#                 print(f"[DETECTED] {name} with confidence {score}%")

#                 if name == "Unknown":
#                     print("[SKIP] Face not matched with known references.")
#                     continue

#                 now = timezone.now()
#                 cutoff = now - timedelta(minutes=1)
#                 if AttendanceRecord.objects.filter(name=name, time__gte=cutoff).exists():
#                     print(f"[SKIP] {name} already logged within 1 minute.")
#                     continue

#                 pil_face = Image.fromarray(face["face_image"])
#                 buffer = ContentFile(b"")
#                 pil_face.save(buffer, format='JPEG')
#                 buffer.seek(0)

#                 record = AttendanceRecord(name=name, accuracy=score)
#                 record.image.save(f"{name}_{now.strftime('%Y%m%d_%H%M%S')}.jpg", buffer, save=True)
#                 record.save()

#                 print(f"[LOGGED] {name} | {score}%")

#         except Exception as e:
#             print("[ERROR]", str(e))

#         time.sleep(1)

#     cap.release()




import cv2
import datetime
import time

rtsp_url = 'rtsp://nabi:demo12345@192.168.2.194:554/h264'
cap = cv2.VideoCapture(rtsp_url)

frame_count = 0
start_time = time.time()

while True:
    success, frame = cap.read()
    if not success:
        continue

    frame_count += 1
    elapsed = time.time() - start_time
    fps = frame_count / elapsed

    # Optional: show FPS
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Print FPS every 50 frames
    if frame_count % 50 == 0:
        print(f"Processed {frame_count} frames, FPS: {fps:.2f}")

    cv2.imshow("RTSP Feed (Check Delay)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()











