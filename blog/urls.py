from django.urls import path
from . import views
from .views import blog_detail


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),
]