from django.contrib import admin

# Register your models here.
from ecommerce.models import Product, Category,ProductColor,ProductImage,ProductSize

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductSize)
admin.site.register(ProductColor)
admin.site.register(ProductImage)