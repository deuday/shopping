from django.contrib import admin
from django.urls import path, include
from .import views

app_name='searchapp'

urlpatterns = [
    path('', views.search_result, name='search_result'),


]
