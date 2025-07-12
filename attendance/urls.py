from django.urls import path
from .views import AttendanceRecordView, video_feed

urlpatterns = [
    path('attendance/', AttendanceRecordView.as_view(), name='attendance'),
    path('video-feed/', video_feed, name='video-feed'),
]
