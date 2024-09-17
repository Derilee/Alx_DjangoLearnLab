from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView
from django.contrib.auth import views


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile')
]