from django.urls import path,include
from rest_framework.routers import DefaultRouter
from ecommerce.views import ProductListView,CategoryListView,ProductCategoryList

router = DefaultRouter()
router.regiset('products',ProductListView)
router.register('category',CategoryListView)
router.register('productcategory',ProductCategoryList)

urlpatterns = [
    path('',include(router.urls)),
    ]