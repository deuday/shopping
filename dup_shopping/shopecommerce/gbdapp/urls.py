from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.contrib import admin
from django.urls import path

app_name = 'gbdapp'
urlpatterns = [

    path('', views.AllProdCat, name='AllProdCat'),
    path('<slug:c_slug>/', views.AllProdCat, name='products_by_category'),
   path('<slug:c_slug>/<slug:product_slug>/', views.AllProdetails, name='prodcatdetail')

]
