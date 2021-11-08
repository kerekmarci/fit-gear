from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_bag, name='bag'),
    path('add_to_bag/<int:product_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove_from_bag/<int:product_id>/', views.remove_from_bag, name='remove_from_bag'),
]