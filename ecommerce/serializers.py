from rest_framework import serializers
from ecommerce.models import Product,Category,ProductCategory
from account.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price','description','image','discount']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['product','category']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','password2','email','phone_number','address']
        extra_kwargs = {"password"}

    def create(self,validated_data):
        user = User(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
    
