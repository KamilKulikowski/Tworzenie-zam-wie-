from django.contrib import admin
from django.urls import path

from customers import views as customer_views
from items import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('user_panel/', customer_views.user_panel, name="user_panel"),
    path('customers/new/', customer_views.customer_create, name="customer_create"),
    path('customers/t/', customer_views.customer_table, name="customer_table"),
    path('customers/<int:pk>/', customer_views.customer_detail, name="customer_detail"),
    path('customers/<int:pk>/edit', customer_views.customer_update, name="customer_update"),
    path('customers/', customer_views.customer_list, name="customer_list"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', customer_views.home, name="home"),

    path('sellers_table/', customer_views.seller_table, name="sellers_table"),
    path('item-create/', views.item_create, name='item_create'),
    path('item-table/', views.items_table, name='items_table'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:item_id>', views.add_to_cart, name="add_to_cart"),
    path('clear_cart/', views.clear_cart, name="clear_cart"),
    path('place_order/', views.place_order, name="place_order"),
    path('orders/', views.orders, name="orders"),
    path('orders/<int:order_id>/', views.order_details, name="order_details"),
]

