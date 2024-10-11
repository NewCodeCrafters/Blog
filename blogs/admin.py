from django.contrib import admin
from .models import BlogsModel


# Register your models here.

@admin.register(BlogsModel)
class BlogsModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = list_display