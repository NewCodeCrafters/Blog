from django import forms
from .models import BlogsModel


class BlogsForm(forms.ModelForm):
    class Meta:
        model = BlogsModel
        fields = '__all__'

