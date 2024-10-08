from django.contrib import admin
from .models import BlogModel
# Register your models here.
@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = list_display


