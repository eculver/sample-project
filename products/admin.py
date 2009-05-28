from django.contrib import admin
from b3breview.products.models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'primary_image', 'slug', 'published', 'publish_on', 'posted_by')

admin.site.register(Product, ProductAdmin)