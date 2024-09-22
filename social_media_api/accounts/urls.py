from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView, follow_userView, unfollow_userView
from django.contrib.auth import views


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/',follow_userView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_userView.as_view(), name='unfollow_user'),
]