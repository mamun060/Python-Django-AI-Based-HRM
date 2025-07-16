import os
import cv2
import torch
import threading
import numpy as np
from PIL import Image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.base import ContentFile
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings
from django.http import StreamingHttpResponse
from attendance.models import AttendanceRecord , DailyAttendanceSummary
from employee.models import Employee
from .serializers import AttendanceRecordSerializer
from .utils.face_recognition import load_reference_embeddings, recognize_faces
from .utils.model_loader import load_yolo_model, load_facenet_model

# Global models
yolo_model = load_yolo_model()
facenet_model = load_facenet_model()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
reference_dir = os.path.join(settings.BASE_DIR, 'media/attendance')
reference_embeddings = load_reference_embeddings(reference_dir, facenet_model.to(device))

def log(msg: str):
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {msg}")

class AttendanceRecordView(APIView):
    def get(self, request, *args, **kwargs):
        records = AttendanceRecord.objects.all().order_by('-time')
        serializer = AttendanceRecordSerializer(records, many=True)
        return Response(serializer.data)


# def run_continuous_face_recognition():
#     try:
#         log("⏳ Starting RTSP face recognition thread...")
#         rtsp_url = 'rtsp://nabi:demo12345@192.168.2.194:554/h264'
#         cap = cv2.VideoCapture(rtsp_url)

#         if not cap.isOpened():
#             log("❌ RTSP stream could not be opened.")
#             return

#         frame_count = 0
#         while True:
#             success, frame = cap.read()
#             if not success:
#                 continue

#             frame_count += 1
#             if frame_count % 3 != 0:
#                 continue

#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             results = yolo_model.predict(source=frame_rgb, conf=0.5, imgsz=640, verbose=False)
#             detected_faces = recognize_faces(frame_rgb, results, facenet_model, reference_embeddings)

#             if detected_faces:
#                 log(f"📸 Detected {len(detected_faces)} face(s).")
#             else:
#                 log("🖕 No faces detected.")

#             for face in detected_faces:
#                 if face['name'] == "Unknown":
#                     continue

#                 name = face['name']
#                 now = timezone.now()
#                 recent = now - timedelta(seconds=1)

#                 if AttendanceRecord.objects.filter(name=name, time__gte=recent).exists():
#                     log(f"⏱️ Skipped: {name} already logged recently.")
#                     continue

#                 pil_face = Image.fromarray(face["face_image"])
#                 buffer = ContentFile(b"")
#                 pil_face.save(buffer, format='JPEG')
#                 buffer.seek(0)

#                 record = AttendanceRecord(name=name, accuracy=face['score'])
#                 record.image.save(f"{name}_{now.strftime('%Y%m%d%H%M%S')}.jpg", buffer, save=True)
#                 record.save()

#                 log(f"✅ Saved: {name} with {face['score']}% accuracy")
#     except Exception as e:
#         log(f"🔥 Thread exception: {e}")


def run_continuous_face_recognition():
    try:
        log("⏳ Starting webcam face recognition thread...")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 🟢 Use your PC webcam

        if not cap.isOpened():
            log("❌ Webcam could not be opened.")
            return

        frame_count = 0
        while True:
            success, frame = cap.read()
            if not success:
                continue

            frame_count += 1
            if frame_count % 3 != 0:
                continue

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = yolo_model.predict(source=frame_rgb, conf=0.5, imgsz=640, verbose=False)
            detected_faces = recognize_faces(frame_rgb, results, facenet_model, reference_embeddings)

            if detected_faces:
                log(f"📸 Detected {len(detected_faces)} face(s).")
            else:
                log("🙈 No faces detected.")

            for face in detected_faces:
                if face['name'] == "Unknown":
                    continue

                name = face['name']
                now = timezone.now()
                recent = now - timedelta(seconds=1)

                if AttendanceRecord.objects.filter(name=name, time__gte=recent).exists():
                    log(f"⏱️ Skipped: {name} already logged recently.")
                    continue

                pil_face = Image.fromarray(face["face_image"])
                buffer = ContentFile(b"")
                pil_face.save(buffer, format='JPEG')
                buffer.seek(0)

                record = AttendanceRecord(name=name, accuracy=face['score'])
                record.image.save(f"{name}_{now.strftime('%Y%m%d%H%M%S')}.jpg", buffer, save=True)
                record.save()

                log(f"✅ Saved: {name} with {face['score']}% accuracy")
    except Exception as e:
        log(f"🔥 Thread exception: {e}")


# Start background thread
threading.Thread(target=run_continuous_face_recognition, daemon=True).start()

# ip camera version for production
# def gen_frames():
#     rtsp_url = 'rtsp://nabi:demo12345@192.168.2.194:554/h264'
#     cap = cv2.VideoCapture(rtsp_url)

#     if not cap.isOpened():
#         raise RuntimeError("RTSP stream can't be opened")

#     while True:
#         success, frame = cap.read()
#         if not success:
#             continue

#         ret, buffer = cv2.imencode('.jpg', frame)
#         if not ret:
#             continue

#         yield (
#             b'--frame\r\n'
#             b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n'
#         )

# webcam version for testing purposes
def gen_frames():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # ✅ DirectShow backend

    if not cap.isOpened():
        raise RuntimeError("Webcam can't be opened")

    while True:
        success, frame = cap.read()
        if not success:
            continue

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n'
        )



def video_feed(request):
    return StreamingHttpResponse(
        gen_frames(),
        content_type='multipart/x-mixed-replace; boundary=frame'
    )


# def update_daily_summary(username):
#     try:
#         employee = Employee.objects.get(username=username)
#     except Employee.DoesNotExist:
#         return

#     today = datetime.today().date()

#     # Get all today's records for this user
#     records = AttendanceRecord.objects.filter(name=username, time__date=today).order_by('time')
#     if not records.exists():
#         return

#     in_time = records.first().time.time()
#     out_time = records.last().time.time()

#     # Calculate total time in hours
#     duration = datetime.combine(today, out_time) - datetime.combine(today, in_time)
#     total_hours = round(duration.total_seconds() / 3600, 2)

#     # Save/update summary
#     summary, created = DailyAttendanceSummary.objects.get_or_create(employee=employee, date=today)
#     summary.in_time = in_time
#     summary.out_time = out_time
#     summary.total_hours = total_hours
#     summary.save()