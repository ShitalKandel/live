from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from ecommerce.models import Product,Category,ProductCategory
from ecommerce.serializers import ProductSerializer,CategorySerializer,ProductCategorySerializer



class ProductListView(ListCreateAPIView):
    qs = Product.objects.all()
    sc = ProductSerializer(qs)

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    qs = Product.objects.all()
    sc = ProductSerializer(qs)

class CategoryListView(ListCreateAPIView):
    qs = Category.objects.all()
    sc = CategorySerializer(qs)

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    qs = Category.objects.all()
    sc = CategorySerializer(qs)

class ProductCategoryList(ListCreateAPIView):
    qs = ProductCategory.objects.all()
    sc = ProductCategorySerializer(qs)

class ProductCategoryDetail(RetrieveUpdateDestroyAPIView):
    qs = ProductCategory.objects.all()
    sc = ProductCategorySerializer(qs)