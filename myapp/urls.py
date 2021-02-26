from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.contrib import auth

from . import views

router = routers.DefaultRouter()
urlpatterns = [
    path('auth',include('rest_framework.urls')),
    path('',include(router.urls))
]

# Client
urlpatterns += [
    path('client', views.ClientListCreate.as_view()),
    path('client/<int:id>', views.CartItemRetrieveUpdateDestroy.as_view())

]

# Merchant
urlpatterns += [
    path('merchant',views.MerchantListCreate.as_view()),
    path('merchant/<int:id>',views.MerchantRetrieveUpdateDestroy.as_view())
]

# Category
urlpatterns += [
    path('category',views.CartListCreate.as_view()),
    path('category/<int:id>',views.CategoryRetrieveUpdateDestroy.as_view())
]

# Product
urlpatterns += [
    path('product',views.ProductListCreate.as_view()),
    path('product/<int:id>',views.ProductRetrieveUpdateDestroy.as_view())
]

# Cart
urlpatterns += [
    path('cart',views.CartListCreate.as_view()),
    path('cart/<int:id>',views.CartRetrieveUpdateDestroy.as_view())
]
# CartItem
urlpatterns += [
    path('cartitem',views.CartItemListCreate.as_view()),
    path('cartitem/<int:id>',views.CartItemRetrieveUpdateDestroy.as_view())
]

# Transaction
urlpatterns += [
    path('transaction',views.TransactionListCreate.as_view()),
    path('transaction/<int:id>',views.CartItemRetrieveUpdateDestroy.as_view())
]