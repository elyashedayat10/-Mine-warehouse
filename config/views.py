from django.shortcuts import render
from django.views.generic import ListView, View
from product.models import ProductBase, ExportalProduct, InternalProduct, LinedProducts, Loaded
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum


# Create your views here.

class HomePage(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            "exportal": ExportalProduct.objects.filter(active=True)[:3],
            "lined": LinedProducts.objects.all()[:3],
            "special_offer": ExportalProduct.objects.filter(is_special=True, active=True)[:3],
            "sliders": ExportalProduct.objects.filter(is_special=True, active=True)[:5],
        }
        return render(request, "config/site_home.html", context)


class PanelHome(View):
    def get(self, request):
        context = {
            "tolid_kol_kharegi": ExportalProduct.objects.all().count(),
            "tolid_kol_dakheli": InternalProduct.objects.all().count(),
            "bargiri_salmas": Loaded.objects.filter(mine__name="سلماس").aggregate(Sum("weight_of_scales")),
            "bargiri_tekab": Loaded.objects.filter(mine__name="تکاب").aggregate(Sum("weight_of_scales")),
            "bargiri_atashkoh": Loaded.objects.filter(mine__name="آتشکوه").aggregate(Sum("weight_of_scales")),
            "bargiri_mahabad": Loaded.objects.filter(mine__name="مهاباد").aggregate(Sum("weight_of_scales")),
        }
        return render(request, "panel/panel.html", context)


class BlockInfo(View):
    def get(self, request):
        return render(request, "config/info.html")
