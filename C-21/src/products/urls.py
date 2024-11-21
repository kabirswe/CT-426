from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product_index'),
    path('category/create/', views.category_create, name='product_category_create'),
    path('category/list/', views.category_list, name='product_category_list'),
]