from django import forms
from .models import Blog
class BlogCreateForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=("title","summary","bold","description","image")
        labels ={
        "title":"عنوان",
        "summary":"خلاصه",
        "bold":"متن بولد",
        "description":"توضیحات",
        "image":"عکس",
        }
        
        
