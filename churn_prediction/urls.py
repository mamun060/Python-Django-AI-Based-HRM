from django.urls import path
from . import views

urlpatterns = [
    path('churn', views.home, name='employee-churn'),
]