from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {"products":products, "categorys":categorys}
    return render(request, "home.html", context)

def contact(request):
    categorys = Category.objects.all()
    context = {"categorys":categorys}
    if request.method == "POST":
        name = request.POST["name_contact"]
        surname = request.POST["surname_contact"]
        email = request.POST["email_contact"]
        comment = request.POST["comment_contact"]

        Contact(
            contact_name=name,
            contact_surname=surname,
            contact_email=email,
            contact_comment=comment,
        ).save()     
        return render(request, "response.html", context)

    return render(request, "contact.html", context)

def category_products(request, id):
    categorys = Category.objects.all()
    cat_pro = Category.objects.get(category_id=id)
    product_cat = Product.objects.filter(product_category=cat_pro)
    context = {"cat_pro":cat_pro,"categorys":categorys, "product_cat":product_cat}
    return render(request, "kategori/category_products.html", context)

def products(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    context = {"products":products,"categorys":categorys}
    return render(request, "kategori/products.html", context)
    
    

def product(request, id):
    categorys = Category.objects.all()
    pro = Product.objects.get(product_id=id)
    context = {"pro":pro, "categorys":categorys}
    return render(request, "kategori/product.html", context)
