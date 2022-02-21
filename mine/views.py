from django.shortcuts import render
from .forms import MineForm
from .models import Mine
from django.views.generic import ListView, CreateView, DetailView, View
from django.urls import reverse_lazy
from django.db.models import Sum


# Create your views here.
# class MineListPanel(ListView):
#     model = Mine
#     template_name = "mine/mine_panel_list.html"


class MineListSite(ListView):
    model = Mine
    template_name = "mine/mine_site_list.html"


class MineDetailPanel(DetailView):
    model = Mine
    slug_field = "pk"
    slug_url_kwarg = "pk"
    template_name = "mine/mine_detail_panel.html"


class MineDetailSite(DetailView):
    model = Mine
    slug_field = "slug"
    slug_url_kwarg = "slug"
    template_name = "mine/mine_site_Detail.html"


class MineCreate(CreateView):
    model = Mine
    template_name = "mine/mine_create.html"
    success_url = reverse_lazy("config:panel_home")
    form_class = MineForm

    def form_invalid(self, form):
        print(form.errors)
        return super(MineCreate, self).form_invalid(form)


class MineLaw(View):
    def get(self, request):
        mine = Mine.objects.all()
        all_law = Mine.objects.all().aggregate(Sum("government_law"))["government_law__sum"]
        context = {
            "info": mine,
            "all_law": all_law
        }
        return render(request, "mine/mine_law.html", context)
