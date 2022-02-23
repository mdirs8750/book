from telnetlib import STATUS
from unicodedata import category
from django.contrib import admin
from .models import clnt_info, order, product ,Category
# from book.apbook.models import uploadimg

# Register your models here.
# class admindtls(admin.ModelAdmin):
#     list_display=['firstname','lastname','email']

admin.site.register(clnt_info)
admin.site.register(product)
admin.site.register(Category)
admin.site.register(order)
