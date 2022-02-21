from django.shortcuts import render
from django.views.generic import ListView,CreateView
# Create your views here.
from .models import Blog
from django.urls import reverse_lazy
from .forms import BlogCreateForm
class BlogListView(ListView):
    model = Blog
    template_name = "blog/list.html"


class BlogPanelListView(ListView):
    model = Blog
    template_name = "blog/panel_list.html"

class BlogCreateView(CreateView):
    form_class=BlogCreateForm
    template_name="blog/create.html"
    success_url=reverse_lazy("blog:blog_list")
    
    
