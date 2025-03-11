from django.shortcuts import render, redirect
from .models import CommunityPost
from .forms import CommunityPostForm
from django.contrib.auth.decorators import login_required

def home(request):
    posts = CommunityPost.objects.all()
    return render(request, 'community/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = CommunityPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) 
            post.author = request.user 
            post.save() 
            return redirect('community_list') 
    else:
        form = CommunityPostForm()
    return render(request, 'community/add_post.html', {'form': form})
def community_list(request):
    posts = CommunityPost.objects.all()
    return render(request, 'community/community_list.html', {'posts': posts})