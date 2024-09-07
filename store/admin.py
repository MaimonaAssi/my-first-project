from django.contrib import admin
from .models import Category, customer, Product, order
admin.site.register(Category)
admin.site.register(customer)
admin.site.register(Product)
admin.site.register(order)
