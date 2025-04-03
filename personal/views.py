from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag, Image, Video, Me, Ability

def home(request):
    posts = Post.objects.all()
    filtered_posts = posts.filter(is_main=True)
    if not request.user.is_superuser:
        filtered_posts = filtered_posts.filter(shown=True)
    sorted_posts = filtered_posts.order_by('-date')
    personal = Me.objects.all()
    return render(request, 'home.html', {'posts': sorted_posts, 'personal': personal})

def hobbies(request):
    posts = Post.objects.all()
    filtered_posts = posts.filter(is_main=False)
    if not request.user.is_superuser:
        filtered_posts = filtered_posts.filter(shown=True)
    sorted_posts = filtered_posts.order_by('-date')
    personal = Me.objects.all()
    return render(request, 'hobbies.html', {'posts': sorted_posts, 'personal': personal})

def personal(request):
    personal = Me.objects.all()
    return render(request, 'personal.html', {'personal': personal})

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post.html', {'post': post})