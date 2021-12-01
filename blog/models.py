from django.db import models
from accounts.models import Account


class Post(models.Model):
    title = models.CharField(max_length=45, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Account, on_delete= models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField('Comment')
    commented_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['commented_on']