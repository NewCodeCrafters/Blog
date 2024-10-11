from django.shortcuts import render, redirect
from .forms import BlogsForm
from .models import BlogsModel



def all_blogs(request):
    blogs = BlogsModel.objects.all()
    
    context = {
        'blogs': blogs
    }

    return render(request, 'blog/all_blogs.html', context)


# Create your views here.

def create_blog(request):
    if request.method =='POST':
        form = BlogsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_blogs')
    else:
        form = BlogsForm()
        
    return render(request, 'blog/create_blog.html', context = {'form': form})