from django.urls import path, include
from app.views import home_views , login_views

urlpatterns = [
    path('', home_views.homeView, name= 'homePage'),
    path('login', login_views.loginView , name="login" )
]