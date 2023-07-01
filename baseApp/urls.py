from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path("register", views.createUser, name="register"),
    path("login", views.loginUser, name="login"),
]
