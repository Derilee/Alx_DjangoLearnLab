from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('post/', views.BlogListView.as_view(), name='posts'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.BlogListView.as_view(), name='posts_list'),
    path('posts/new/', views.BlogCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
]