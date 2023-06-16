from django import forms  
from .models import ProdCategory


class ProdCategoryForm(forms.ModelForm):  
    class Meta:  
        model = ProdCategory
        fields = ["category", "description", "image"]