from django.contrib import admin
from .models import Products,customers,gstResults

# Register your models here.

admin.site.register(Products)
admin.site.register(customers)
admin.site.register(gstResults)
