from django.urls import path
from AdminApp import views

urlpatterns = [
    path('',views.home,name='home_admin'),
    path('add_product',views.add_products,name='add_product'),
    path('add_specification',views.add_specification,name='add_specification'),
    path('add_brand',views.brand,name='add_brand'),
    path('add_condition',views.condition,name='add_condition'),
    path('add_category',views.category,name='add_category'),
    path('add_image',views.images,name='add_image'),
    path('products_list',views.products_list, name='products_list'),
    path('remove/<int:product_id>',views.remove_products,name='remove_products'),
    path('add_users',views.add_user,name='add_users'),
    path('users_list',views.users_list,name='users_list'),
    path('remove_user/<int:user_id>',views.remove_users,name='remove_users'),

]