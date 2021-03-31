from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'





class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        # fields = '__all__'

        exclude = ['lft','rght','tree_id']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):

    """
    GET
    POST
    """
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'






