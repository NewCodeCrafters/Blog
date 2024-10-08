from django.urls import path
from . import views


urlpatterns = [
    path('view_blogs', views.view_blogs, name='view_blogs')
]
