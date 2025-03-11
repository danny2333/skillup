from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# Authentication Views
def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    """
    Handles user login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('home') 
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    """
    Handles user logout.
    """
    logout(request)
    return redirect('home')  # Redirect to the home page after logout


# Profile Views
@login_required
def profile(request):
    """
    Displays the user's profile.
    """
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    """
    Handles editing the user's profile.
    """
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/edit_profile.html', {'form': form})