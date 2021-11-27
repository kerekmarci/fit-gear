from django.urls import path
from . import views


urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('success/<str:order_id>', views.success, name='success'),
]
