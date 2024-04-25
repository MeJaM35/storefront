from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('product/', views.product, name='product'),
    path('seller_register/', views.sellerRegister, name='sellerRegister'),
    path('user_register/', views.userRegister, name='userRegister'),
    path('login/', views.Login, name='Login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('product_page/', views.ProductPage, name='ProductPage'),
    path('profile/', views.user_profile, name='user_profile'),
    path('seller_profile/', views.seller_profile, name='seller_profile'),
    path('logout', views.logoutUser, name='logout'),
]