from operator import concat
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, null=True, blank=True)
    category_image = models.ImageField(upload_to="media/", null=True, blank=True)
    category_alt = models.TextField(max_length=700, null=True, blank=True)

    def __str__(self):
        return f"{self.category_name}"


class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    material_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"{self.material_name}"

class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"{self.color_name}"

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50, null=True, blank=True)
    product_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    product_review = models.TextField(max_length=400, null=True, blank=True)
    product_text = models.TextField(max_length=700, null=True, blank=True)
    product_sale = models.IntegerField(null=True, blank=True)
    product_alt = models.TextField(max_length=700, null=True, blank=True)
    product_material = models.ManyToManyField(Material, blank=True)
    product_color = models.ManyToManyField(Color, blank=True)
    product_garanci = models.IntegerField(null=True, blank=True)
    product_wateresistent = models.IntegerField(null=True, blank=True)
    product_image = models.ImageField(upload_to="media/" ,null=True, blank=True)
    product_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"



class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=50, null=True, blank=True)
    contact_surname = models.CharField(max_length=150, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_comment = models.TextField(max_length=700, null=True, blank=True)
    
    def __str__(self):
        return f"{self.contact_name}"
