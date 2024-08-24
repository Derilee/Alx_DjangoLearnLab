from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileView, SignUpView
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),  # User signup
    path('profile/', ProfileView.as_view(), name='profile'),  # User profile
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # User login
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),  # User logout
]
