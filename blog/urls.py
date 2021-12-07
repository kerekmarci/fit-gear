from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('add/add_blogpost/', views.add_blogpost, name='add_blogpost'),
]
