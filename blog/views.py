from django.shortcuts import render
from .models import BlogModel

# Create your views here.

def view_blogs(request):
    blogs = BlogModel.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/view_blogs.html', context)