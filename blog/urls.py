from django.urls import path
from . import views

urlpatterns = [
    path('get_blogs/', views.get_blogs, name ='get_blogs'),
    path('specific_blogs/', views.specific_blogs, name='specific_blogs')
]
