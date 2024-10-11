from django.db import models

# Create your models here.

class BlogsModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    content = models.TextField()