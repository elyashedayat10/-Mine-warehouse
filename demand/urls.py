from django.urls import path
from .views import HoldListView, VisitListView, SampleListView

app_name = "demand"
urlpatterns = [
    path("sample_list/", SampleListView.as_view(), name="sample_list"),
    path("hold_list/", HoldListView.as_view(), name="hold_list"),
    path("visit_list/", VisitListView.as_view(), name="visit_list")
]
