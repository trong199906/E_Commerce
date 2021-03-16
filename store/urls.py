from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('Cart', views.cart, name='cart'),
    path('Checkout', views.checkout, name='checkout'),
    path('update_item/', views.updated_item, name='update_item')
]