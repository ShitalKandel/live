from django.db import models
# from django.contrib.auth.models import AbstractUser
from base.models import BaseModel
from django.utils.text import slugify




class Category(BaseModel):
    category_name = models.CharField(max_length=200,null=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category_image = models.ImageField(upload_to='categories',null=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    product_name = models.CharField(max_length=200,null=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE,related_name="products",default=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    discount = models.FloatField(blank=True,null=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.product_name)
        super(Product,self).self(*args,**kwargs)


    def __str__(self):
        return self.product_name
    

class ProductColor(BaseModel):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self) ->str:
        return self.color_name
    
class ProductSize(BaseModel):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self) ->str:
        return self.size_name

class ProductImage(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_image")
    image = models.ImageField(upload_to="product")