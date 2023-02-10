from django.contrib import admin
from .models import ProductsDescriptionVinyl, ProductsDescriptionHiFi

# ProductsDescriptionHifi
# from django.utils.html import format_html
# Register your models here.
admin.site.register(ProductsDescriptionVinyl)
admin.site.register(ProductsDescriptionHiFi)

# @admin.register(ProductsDescriptionVinyl)
# class VinylAdmin(admin.ModelAdmin):
#     def thumbnail(self, object):
#         html_code = '<img srv = "{}" width = "40" style="border-radius: 50px;"/>'
#         return format_html(html_code.format(object.photo.url))
#
#     inlines = [ProductsDescriptionVinyl]
#     class Meta:
#         model = ProductsDescriptionVinyl