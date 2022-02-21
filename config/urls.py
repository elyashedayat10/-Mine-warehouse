from django.urls import path
from .views import HomePage, PanelHome, BlockInfo

app_name = "config"

urlpatterns = [
    path("config/", HomePage.as_view(), name="site_home"),
    path("panel/", PanelHome.as_view(), name="panel_home"),
    path("info/", BlockInfo.as_view(), name="info"),
]
