from django.contrib import admin
from .models import *
# # # Register your models here.

admin.site.register(User)
admin.site.register(Blog)

# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
#     list_display = ['page_name','page_cat','page_publish_date','user']
