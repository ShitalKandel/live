from django.shortcuts import render
from ecommerce.models import Product


def index(request):
    context = {'product':Product.objects.all()}
    return render(request,'home/index.html',context)