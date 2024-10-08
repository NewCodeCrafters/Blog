from django.db import models

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
