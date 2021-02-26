from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class MerchantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Merchant
        exclude = ['is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions',
                   'last_login']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['lft','right','tree_id']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

