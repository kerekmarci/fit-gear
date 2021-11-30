from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponse

"""
Concept inspired by this website:
https://djangocentral.com/building-a-blog-application-with-django/
"""


def blog(request):
    blogposts = Post.objects.all()
    context = {
        'blogposts': blogposts,
    }
    return render(request, 'blog.html', context)


def blog_detail(request, slug):
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

"""
def add_blogpost(request):
    return render(request, 'add_blogpost.html')
"""