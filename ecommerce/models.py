from django.db import models
# from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class ProductCategory(models.Model):
    prodcut = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)