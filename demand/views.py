from django.shortcuts import render
from .models import Hold, Visit, Sample
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class SampleListView(LoginRequiredMixin, ListView):
    model = Sample

    def get_context_data(self, *args, **kwargs):
        context = super(SampleListView, self).get_context_data(*args, **kwargs)
        context["sample_count"] = Sample.objects.all().count()
        return context

    template_name = "demand/sample_list.html"


class HoldListView(LoginRequiredMixin, ListView):
    model = Hold

    def get_context_data(self, *args, **kwargs):
        context = super(HoldListView, self).get_context_data(*args, **kwargs)
        context["hold_count"] = Hold.objects.all().count()
        return context

    template_name = "demand/hold_list.html"


class VisitListView(LoginRequiredMixin, ListView):
    model = Visit

    def get_context_data(self, *args, **kwargs):
        context = super(VisitListView, self).get_context_data(*args, **kwargs)
        context["visit_count"] = Visit.objects.all().count()
        return context

    template_name = "demand/visit_list.html"
