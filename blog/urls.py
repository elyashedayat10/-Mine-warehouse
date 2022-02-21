from django.urls import path
from .views import BlogListView, BlogPanelListView,BlogCreateView

app_name = "blog"
urlpatterns = [
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_panel_list/", BlogPanelListView.as_view(), name="blog_panel_list"),
    path("blog_create/", BlogCreateView.as_view(), name="create"),
]
