from django.urls import path
from .views import MineCreate, MineListSite, MineDetailSite, MineDetailPanel, MineLaw

app_name = "mine"

urlpatterns = [
    path("create/", MineCreate.as_view(), name="create"),
    path("mine_detail_panel/<int:pk>/", MineDetailPanel.as_view(), name="panel_detail"),
    path("mine_detail_site/<int:pk>/", MineDetailSite.as_view(), name="site_detail"),
    path("list/", MineListSite.as_view(), name="list"),
    path("mine_law/", MineLaw.as_view(), name="mine_law"),
]
