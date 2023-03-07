from django.contrib import admin
from django.urls import path, include
from .import views

app_name='shopping_cart'

urlpatterns = [
    path('add/<int:Product_id>/',views.add_cart,name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:Product_id>/',views.cart_remove,name='cart_remove'),
    path('Item_Delete/<int:Product_id>/',views.Item_Delete,name='Item_Delete')


]
