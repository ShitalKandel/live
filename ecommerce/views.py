from rest_framework import viewsets
from ecommerce.models import Category, Product, ProductColor, ProductSize, ProductImage
from ecommerce.serializers import CategorySerializer, ProductSerializer, ProductColorSerializer, ProductSizeSerializer, ProductImageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication]


class ProductColorViewSet(viewsets.ModelViewSet):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication]



class ProductSizeViewSet(viewsets.ModelViewSet):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication]



class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication]


