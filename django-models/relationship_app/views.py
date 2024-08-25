from django.shortcuts import render
from .models import Book

# Create your views here.


def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'books/list_books.html', context)



from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout
# from django.contrib.auth import login
from django.shortcuts import redirect

# Registration view
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

# Login view
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Logout view
class CustomLogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')
    
    def get(self, request):
        return redirect('login') 

# Profile view, requires login
@method_decorator(login_required, name='dispatch')
class ProfileView(generic.TemplateView):
    template_name = 'profile.html'

class HomeView(TemplateView):
    template_name = 'home.html'
