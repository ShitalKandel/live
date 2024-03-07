from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ecommerce import views
from account.views import UserViewSet,ProfileViewSet


router = DefaultRouter()
router.register('categories', views.CategoryViewSet,basename='categories')
router.register('products', views.ProductViewSet,basename='products')
router.register('product-colors', views.ProductColorViewSet,basename='product_colors')
router.register('product-sizes', views.ProductSizeViewSet,basename='product-size')
router.register('product-images', views.ProductImageViewSet,basename='product-images')
router.register('login',UserViewSet,basename='user_login')
router.register('profile',ProfileViewSet,basename='user_profile')

urlpatterns = [
    path('', include(router.urls)),
]
