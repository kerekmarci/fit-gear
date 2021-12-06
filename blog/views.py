from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.http import HttpResponse
from django.utils.text import slugify

"""
Concept inspired by this website:
https://djangocentral.com/building-a-blog-application-with-django/
"""


def blog(request):
    """
    This view will retrivew all Success Story blog posts
    """
    blogposts = Post.objects.all()
    context = {
        'blogposts': blogposts,
    }
    return render(request, 'blog.html', context)


def blog_detail(request, slug):
    """
    This view will open the full blog post on a separate page
    """
    allposts = Post.objects.all()
    blogposts = Post.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = request.user.first_name
            comment.email = request.user
            comment.post = blogposts
            comment.save()

            return redirect('blog_detail', slug=blogposts.slug)
    else:
        form = CommentForm()

    context = {
        'allposts': allposts,
        'blogposts': blogposts,
        'form': form,
    }
    return render(request, 'blog_detail.html', context)


def add_blogpost(request):
    """
    This view will allow user to add a new Success Story blog post
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.author = request.user
            post.save()
            return redirect('blog')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'add_blogpost.html', context)
