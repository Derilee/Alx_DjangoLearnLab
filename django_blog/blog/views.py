from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserProfileForm, UserProfileExtendedForm
from .models import UserProfile
from django.views import generic, View


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/base.html', {'form':form})

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
