from .models import Category
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Category Name'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
