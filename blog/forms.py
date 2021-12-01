from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        widgets = {
            'body': forms.Textarea(attrs={
            'placeholder': 'Share your success story here...',
            'rows': '3',
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            'body': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Share your thoughts here...',
            'rows': '3',
            })
        }