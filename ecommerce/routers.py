from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ecommerce import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'product-colors', views.ProductColorViewSet)
router.register(r'product-sizes', views.ProductSizeViewSet)
router.register(r'product-images', views.ProductImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
