from django.urls import path,include
from rest_framework.routers import DefaultRouter
from ecommerce.views import ProductListView,CategoryListView,ProductCategoryView

router = DefaultRouter()
router.register('products',ProductListView,basename='product')
router.register('category',CategoryListView,basename='category')
router.register('productcategory',ProductCategoryView,basename='productcategory')

urlpatterns = [
    path('',include(router.urls)),
    ]