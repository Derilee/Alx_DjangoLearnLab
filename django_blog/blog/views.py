from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm, UserProfileForm, UserProfileExtendedForm, CreateUpdateBlogPost, CommentForm
from .models import UserProfile, Post, Comment
from django.views import generic, View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form':form})

@login_required
def profile (request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileExtendedForm(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserProfileForm(instance=request.user)
        profile_form = UserProfileExtendedForm(instance=user_profile)
    return render(request, 'blog/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

class BlogListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


@method_decorator(login_required, name='dispatch')
class BlogCreateView(CreateView):
    model = Post
    form_class = CreateUpdateBlogPost
    template_name = 'blog/post_create.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = CreateUpdateBlogPost
    template_name = 'blog/post_update.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

    def form_valid(self, form):
        form.instance.post = Post.objects.get(id=self.kwargs['post_id'])
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
    
    def get_object(self):
        return Comment.objects.get(id=self.kwargs['comment_id'])

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk':self.object.post.pk})

    def get_object(self):
        return Comment.objects.get(id=self.kwargs['comment_id'])
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
