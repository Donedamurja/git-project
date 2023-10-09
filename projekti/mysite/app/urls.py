from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('category_products/<id>', views.category_products, name='category_products'),
    path('products/', views.products, name='products'),
    path('product/<id>', views.product, name='product'),
]