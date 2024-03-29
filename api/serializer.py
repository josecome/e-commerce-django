from rest_framework import serializers
from contents.models import (
    ProdCategory,
    Product,
    Cart,
)

class ProdCategorySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    
    class Meta:        
        model = ProdCategory
        fields = ["id", "link","category", "image", "username", "category", "first_name", "last_name", "date_created"]


class ProductSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Product
        fields = ["id", "product", "price", "image", "category", "username", "first_name", "last_name", "date_created"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"