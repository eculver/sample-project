from django.contrib import admin
from b3breview.products.models import Product

class ProductAdmin(admin.ModelAdmin):
	pass

admin.site.register(Product, ProductAdmin)