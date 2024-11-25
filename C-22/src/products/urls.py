from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product_index'),
    path('category/create/', views.category_create, name='product_category_create'),
    path('category/<int:category_id>/', views.category_detail, name='product_category_detail'),
    path('category/list/', views.category_list, name='product_category_list'),
    path('category/update/<int:category_id>/', views.category_update, name='product_category_update'),
    path('category/delete/<int:category_id>/', views.category_delete, name='product_category_delete'),
]