from django.shortcuts import render

def get_blogs(request):
    context = {
        'fruits': ['Apple', 'Banana', 'Kiwi', 'Mango', 'Watermelon']
    }
    return render(request, 'blog/get_blogs.html', context)

def specific_blogs(request):
    return render(request, 'blog/specific_blogs.html')
