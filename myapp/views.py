from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
# Create your views here.


# Client
class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

# Merchant

class MerchantListCreate(generics.ListCreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

class MerchantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

# Cart
class CartListCreate(generics.ListCreateAPIView):
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