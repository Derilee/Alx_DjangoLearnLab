from django.urls import path
from .views import CustomLoginView, CustomLogoutView, SignUpView
from .views import HomeView
# from .views import LoginView, LogoutView
# from .views import views
# SignUpView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='register'),
    # path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    # path('login/', LoginView.as_view(template_name='login'), 'login'),
    # path('login/', LogoutView.as_view(template_name='logout'), 'logout'),
]
