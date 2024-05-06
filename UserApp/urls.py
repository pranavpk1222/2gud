from django.urls import path
from UserApp import views

urlpatterns = [
    path('', views.home,name='home'),
    path('search',views.search,name='search'),
    path('detail/<int:product_id>',views.product_details,name='detail'),
    path('user_register',views.user_register,name='user_register'),
    path('login',views.login,name='login'),
    path('cart/<int:spec_id>', views.cart, name='cart'),
    path('cart_store',views.cart_show,name='cart_store'),
    path('logout',views.logout,name='logout'),
    path('remove/<int:cart_id>', views.remove_cart),
    path('detail/favorite/<int:product_id>', views.wishlist),
    path('wish_store',views.wishlist_store,name='wish_store'),
    path('remove_wishlist/<int:favorite_id>', views.remove_wishlist),
    path('profile',views.profile,name='profile'),
    path('address',views.address,name='address'),
    path('update_address/<int:address_id>',views.update_address,name='update_address'),
    path('newaddress',views.new_address,name='newaddress'),
    path('remove_address/<int:address_id>',views.remove_address),
    path('order_first/<int:spec_id>/', views.order_first, name='order_first'),
    path('order_first/ordering_products/<int:spec_id>', views.ordering_products, name='ordering_products'),
    path('my_orders',views.my_orders,name='my_orders'),
    path('detail/review/<int:spec_id>',views.review_order),
    path('eventpage',views.event,name='event_page'),
    path('super_sale/<int:event_id>',views.super_sale),
    path('super_sale/detail/<int:product_id>', views.product_details, name='super_sale_detail')
    # Add more paths as needed
]
