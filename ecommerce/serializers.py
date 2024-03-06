from rest_framework import serializers
from ecommerce.models import Product,Category,ProductCategory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price','description','image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = Category
        fields = ['name']

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = ProductCategory
        fields = ['product','category']