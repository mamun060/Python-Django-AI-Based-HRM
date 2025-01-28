from django.urls import path, include
from app.views import home_views

urlpatterns = [
    path('', home_views.homeView, name= 'homePage')
]