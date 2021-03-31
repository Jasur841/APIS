from django.shortcuts import render
from django.views.decorators.http import require_POST
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from .models import *
from rest_framework import generics, status
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.


# Client
class ClientListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


# Category
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


# Product
class ProductListCreate(generics.ListCreateAPIView):
    permissions_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class CartListCreate(generics.ListCreateAPIView):
    '''
    get:
    Client uzbekcha.

    This is a description from a class level docstring.

    post:
    Client List serialized as JSON.

    This is a description from a class level docstring.

    '''
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


# CartItem
class CartItemListCreate(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemRetrieveUpdateDestroy(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


# Transaction
class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer


class TransactionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
