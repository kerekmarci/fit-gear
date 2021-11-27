from django.urls import path
from . import views


urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('success/<str:order_pk>', views.success, name='success'),
]
