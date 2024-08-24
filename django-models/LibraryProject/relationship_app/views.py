from django.shortcuts import render
from .models import Book

# Create your views here.


def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'books/list_books.html', context)




from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

@method_decorator(login_required, name='dispatch')
class ProfileView(generic.TemplateView):
    template_name = 'profile.html'



from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'