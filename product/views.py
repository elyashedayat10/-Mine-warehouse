from django.shortcuts import render, redirect, get_object_or_404
from tablib import Dataset
from account.models import User
from demand.models import HoldForm, SampleForm, VisitForm, Hold, Visit, Sample
from .filters import ProductFilter, LoadedFilter, DomesticFilter, ExportalFilter, RejectedFilter
from django.views.generic import ListView, View
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .resources import *
from django.db.models import Sum
import os
from pathlib import Path
from .forms import ExportalFileForm, ExportalFileLogoForm, InternalFileLogoForm, InternalFileForm


class LinedProductCreateView(View, LoginRequiredMixin):
    def get(self, request):
        return render(request, "product/create_lined.html")

    def post(self, request):
        imported_data = Dataset().load(request.FILES['file'].read(), format='xlsx')
        lined_product = LinedProducts.objects.create()
        for data in imported_data:
            try:
                internal_product = InternalProduct.objects.get(serial_number_of_the_peak_in_the_mine=data[2])
                obj = LinedProductMember()
                obj.approximate_tonnage = internal_product.approximate_tonnage
                obj.unique_id = internal_product.unique_id
                obj.lined_product = lined_product
            except:
                print('err')
                continue
        return render(request, "product/create_lined.html")


class SpecialOfferList(View):
    def get(self, request):
        special_internal = InternalProduct.objects.filter(is_special=True, active=True)[:10]
        special_exportal = ExportalProduct.objects.filter(is_special=True, active=True)[:10]
        return render(request, "product/special_offer_list.html",
                      {"exportal_list": special_exportal, "special_internal": special_internal})


class SpecialOfferListComplete(View):
    def get(self, request):
        special_internal = InternalProduct.objects.filter(is_special=True, active=True)[:10]
        special_exportal = ExportalProduct.objects.filter(is_special=True, active=True)[:10]
        return render(request, "product/special_offer_complete_list.html",
                      {"exportal_list": special_exportal, "special_internal": special_internal})


def MainPictureExportalCreateView(request):
    if request.method == "POST":
        BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
        print(os.path.join(BASE_DIR, 'ali/file_dir'))
        form = ExportalFileLogoForm(request.POST, request.FILES)
        if form.is_valid():
            file = ExportalMainPicFile(file=form.cleaned_data["file"])
            file.save()
            return redirect("config:panel_home")


def MainPictureExportalCreateView(request):
    if request.method == "POST":
        BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
        print(os.path.join(BASE_DIR, 'ali/file_dir'))
        form = ExportalFileLogoForm(request.POST, request.FILES)
        if form.is_valid():
            file = ExportalMainPicFile(file=form.cleaned_data["file"])
            file.save()
            return redirect("config:panel_home")


def PartialPictureExportalCreateView(request):
    if request.method == "POST":
        form = ExportalFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = ExportalGalleriesFile(file=form.cleaned_data["file"])
            file.save()
            return redirect("config:panel_home")


class AllProductList(LoginRequiredMixin, View):
    def get(self, request):
        base_count = ProductBase.objects.all().count()
        lined_count = LinedProducts.objects.all().count()
        total_count = base_count + lined_count
        total_ton = ProductBase.objects.aggregate(Sum("approximate_tonnage"))['approximate_tonnage__sum']
        # stone_name = request.GET.get("stone_name")
        # stone_type = request.GET.get("stone_type")
        # color = request.GET.get("color")
        # mine = request.GET.get("mine")
        # grade = request.GET.get("grade")
        # if stone_name or stone_type or color or mine or grade:
        #     internal = InternalProduct.objects.filter(mine__stone_type=stone_type, stone_name=stone_name,
        #                                               mine__name=mine, grading_code=grade)
        #     exportal = ExportalProduct.objects.filter(mine__stone_type=stone_type, stone_name=stone_name,
        #                                               mine__name=mine, grading_code=grade, color_code=color)
        context = {
            "internal": InternalProduct.objects.all(),
            "exportal": ExportalProduct.objects.all(),
            "lined": LinedProducts.objects.all(),
            "total_count": total_count,
            "total_ton": total_ton
        }
        return render(request, "product/all_product_complete.html", context)


class AllProductListComplete(LoginRequiredMixin, View):
    def get(self, request):
        base_count = ProductBase.objects.all().count()
        lined_count = LinedProducts.objects.all().count()
        total_count = base_count + lined_count
        total_ton = ProductBase.objects.aggregate(Sum("approximate_tonnage"))['approximate_tonnage__sum']
        # stone_name = request.GET.get("stone_name")
        # stone_type = request.GET.get("stone_type")
        # color = request.GET.get("color")
        # mine = request.GET.get("mine")
        # grade = request.GET.get("grade")
        # if stone_name or stone_type or color or mine or grade:
        #     internal = InternalProduct.objects.filter(mine__stone_type=stone_type, stone_name=stone_name,
        #                                               mine__name=mine, grading_code=grade)
        #     exportal = ExportalProduct.objects.filter(mine__stone_type=stone_type, stone_name=stone_name,
        #                                               mine__name=mine, grading_code=grade, color_code=color)
        context = {
            "internal": InternalProduct.objects.all(),
            "exportal": ExportalProduct.objects.all(),
            "lined": LinedProducts.objects.all(),
            "total_count": total_count,
            "total_ton": total_ton
        }
        return render(request, "product/all_product_complete.html", context)


class InternalProductPanelList(ListView):
    model = InternalProduct
    template_name = "product/internal_list_panel.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super(InternalProductPanelList, self).get_context_data(*args, **kwargs)
        context_data["total"] = InternalProduct.objects.all().count()
        context_data["tonajze"] = InternalProduct.objects.all().aggregate(Sum("approximate_tonnage"))[
            'approximate_tonnage__sum']
        return context_data


def product_detail(request, unique_id):
    context = {"full_path": request.build_absolute_uri() + '?share=1'}
    if request.resolver_match.url_name == 'internal_product_detail':
        context.update({'object': get_object_or_404(InternalProduct, unique_id=unique_id), 'is_internal': 1})
    elif request.resolver_match.url_name == 'exportal_product_detail':
        context.update({'object': get_object_or_404(ExportalProduct, unique_id=unique_id), 'is_exportal': 1})
    if request.method == 'POST':
        if request.POST.get('submit') == 'hold':
            form = HoldForm(request.POST, request.FILES)
            context.update({'form': form})
            if form.is_valid():
                obj = Hold()
                obj.user = User.objects.get(id=request.user.id)
                if form.cleaned_data['pin']:
                    obj.pin = form.cleaned_data['pin']
                if len(request.POST.getlist('field')) > 0:
                    if len(request.POST.getlist('field')[1]) <= 0:
                        if request.POST.getlist('field')[0] == 'stone_cutting_factory':
                            obj.field = 'کارخانه سنگ بری'
                        if request.POST.getlist('field')[0] == 'export':
                            obj.field = 'صادرات'
                        if request.POST.getlist('field')[0] == 'block_warehouse':
                            obj.field = 'انبار بلوک'
                        if request.POST.getlist('field')[0] == 'internal_sales_of_blocks':
                            obj.field = 'فروش داخلی بلوک'
                    else:
                        obj.field = request.POST.getlist('field')[1]
                if form.cleaned_data['tonnage']:
                    obj.tonnage = form.cleaned_data['tonnage']
                if form.cleaned_data['phone']:
                    obj.phone = form.cleaned_data['phone']
                if form.cleaned_data['email']:
                    obj.email = form.cleaned_data['email']
                if form.cleaned_data['male']:
                    if form.cleaned_data['male'] == 'true':
                        obj.male = True
                    else:
                        obj.male = False
                if form.cleaned_data['first_name']:
                    obj.first_name = form.cleaned_data['first_name']
                if form.cleaned_data['last_name']:
                    obj.last_name = form.cleaned_data['last_name']
                if form.cleaned_data['description']:
                    obj.description = form.cleaned_data['description']
                if form.cleaned_data['file']:
                    obj.file = form.cleaned_data['file']
                obj.save()
        if request.POST.get('submit') == 'visit':
            form = VisitForm(request.POST, request.FILES)
            context.update({'form': form})
            if form.is_valid():
                obj = Visit()
                obj.user = User.objects.get(id=request.user.id)
                if len(request.POST.getlist('field')) > 0:
                    if len(request.POST.getlist('field')[1]) <= 0:
                        if request.POST.getlist('field')[0] == 'stone_cutting_factory':
                            obj.field = 'کارخانه سنگ بری'
                        if request.POST.getlist('field')[0] == 'export':
                            obj.field = 'صادرات'
                        if request.POST.getlist('field')[0] == 'block_warehouse':
                            obj.field = 'انبار بلوک'
                        if request.POST.getlist('field')[0] == 'internal_sales_of_blocks':
                            obj.field = 'فروش داخلی بلوک'
                    else:
                        obj.field = request.POST.getlist('field')[1]
                if form.cleaned_data['tonnage']:
                    obj.tonnage = form.cleaned_data['tonnage']
                if form.cleaned_data['male']:
                    if form.cleaned_data['male'] == 'true':
                        obj.male = True
                    else:
                        obj.male = False
                if form.cleaned_data['first_name']:
                    obj.first_name = form.cleaned_data['first_name']
                if form.cleaned_data['last_name']:
                    obj.last_name = form.cleaned_data['last_name']
                if form.cleaned_data['occupation']:
                    obj.occupation = form.cleaned_data['occupation']
                if form.cleaned_data['company']:
                    obj.company = form.cleaned_data['company']
                if form.cleaned_data['phone']:
                    obj.phone = form.cleaned_data['phone']
                if form.cleaned_data['email']:
                    obj.email = form.cleaned_data['email']
                if form.cleaned_data['address']:
                    obj.address = form.cleaned_data['address']
                if form.cleaned_data['visit_date']:
                    obj.visit_date = form.cleaned_data['visit_date']
                if form.cleaned_data['visit_hour']:
                    obj.visit_hour = form.cleaned_data['visit_hour']
                if form.cleaned_data['visit_minute']:
                    obj.visit_minute = form.cleaned_data['visit_minute']
                if form.cleaned_data['description']:
                    obj.description = form.cleaned_data['description']
                if form.cleaned_data['file']:
                    obj.file = form.cleaned_data['file']
                obj.save()
        if request.POST.get('submit') == 'sample':
            form = SampleForm(request.POST, request.FILES)
            context.update({'form': form})
            if form.is_valid():
                obj = Sample()
                obj.user = User.objects.get(id=request.user.id)
                if form.cleaned_data['pin']:
                    obj.pin = form.cleaned_data['pin']
                if len(request.POST.getlist('field')) > 0:
                    if len(request.POST.getlist('field')[1]) <= 0:
                        if request.POST.getlist('field')[0] == 'stone_cutting_factory':
                            obj.field = 'کارخانه سنگ بری'
                        if request.POST.getlist('field')[0] == 'export':
                            obj.field = 'صادرات'
                        if request.POST.getlist('field')[0] == 'block_warehouse':
                            obj.field = 'انبار بلوک'
                        if request.POST.getlist('field')[0] == 'internal_sales_of_blocks':
                            obj.field = 'فروش داخلی بلوک'
                    else:
                        obj.field = request.POST.getlist('field')[1]
                if form.cleaned_data['tonnage']:
                    obj.tonnage = form.cleaned_data['tonnage']
                if form.cleaned_data['phone']:
                    obj.phone = form.cleaned_data['phone']
                if form.cleaned_data['email']:
                    obj.email = form.cleaned_data['email']
                if form.cleaned_data['male']:
                    if form.cleaned_data['male'] == 'true':
                        obj.male = True
                    else:
                        obj.male = False
                if form.cleaned_data['first_name']:
                    obj.first_name = form.cleaned_data['first_name']
                if form.cleaned_data['last_name']:
                    obj.last_name = form.cleaned_data['last_name']
                if form.cleaned_data['description']:
                    obj.description = form.cleaned_data['description']
                if form.cleaned_data['file']:
                    obj.file = form.cleaned_data['file']
                obj.save()
    return render(request, "product/product_detail.html", context)


def product_detail_lined(request, unique_id):
    context = {"full_path": request.build_absolute_uri() + '?share=1'}
    context.update({'object': get_object_or_404(LinedProducts, unique_id=unique_id)})
    if request.method == 'POST':
        if request.POST.get('submit') == 'hold':
            form = HoldForm(request.POST, request.FILES)
            context.update({'form': form})
            if form.is_valid():
                obj = Hold()
                obj.user = User.objects.get(id=request.user.id)
                if form.cleaned_data['pin']:
                    obj.pin = form.cleaned_data['pin']
                if len(request.POST.getlist('field')) > 0:
                    if len(request.POST.getlist('field')[1]) <= 0:
                        if request.POST.getlist('field')[0] == 'stone_cutting_factory':
                            obj.field = 'کارخانه سنگ بری'
                        if request.POST.getlist('field')[0] == 'export':
                            obj.field = 'صادرات'
                        if request.POST.getlist('field')[0] == 'block_warehouse':
                            obj.field = 'انبار بلوک'
                        if request.POST.getlist('field')[0] == 'internal_sales_of_blocks':
                            obj.field = 'فروش داخلی بلوک'
                    else:
                        obj.field = request.POST.getlist('field')[1]
                if form.cleaned_data['tonnage']:
                    obj.tonnage = form.cleaned_data['tonnage']
                if form.cleaned_data['phone']:
                    obj.phone = form.cleaned_data['phone']
                if form.cleaned_data['email']:
                    obj.email = form.cleaned_data['email']
                if form.cleaned_data['male']:
                    if form.cleaned_data['male'] == 'true':
                        obj.male = True
                    else:
                        obj.male = False
                if form.cleaned_data['first_name']:
                    obj.first_name = form.cleaned_data['first_name']
                if form.cleaned_data['last_name']:
                    obj.last_name = form.cleaned_data['last_name']
                if form.cleaned_data['description']:
                    obj.description = form.cleaned_data['description']
                if form.cleaned_data['file']:
                    obj.file = form.cleaned_data['file']
                obj.save()
        if request.POST.get('submit') == 'visit':
            form = VisitForm(request.POST, request.FILES)
            context.update({'form': form})
            if form.is_valid():
                obj = Visit()
                obj.user = User.objects.get(id=request.user.id)
                if len(request.POST.getlist('field')) > 0:
                    if len(request.POST.getlist('field')[1]) <= 0:
                        if request.POST.getlist('field')[0] == 'stone_cutting_factory':
                            obj.field = 'کارخانه سنگ بری'
                        if request.POST.getlist('field')[0] == 'export':
                            obj.field = 'صادرات'
                        if request.POST.getlist('field')[0] == 'block_warehouse':
                            obj.field = 'انبار بلوک'
                        if request.POST.getlist('field')[0] == 'internal_sales_of_blocks':
                            obj.field = 'فروش داخلی بلوک'
                    else:
                        obj.field = request.POST.getlist('field')[1]
                if form.cleaned_data['tonnage']:
                    obj.tonnage = form.cleaned_data['tonnage']
                if form.cleaned_data['male']:
                    if form.cleaned_data['male'] == 'true':
                        obj.male = True
                    else:
                        obj.male = False
                if form.cleaned_data['first_name']:
                    obj.first_name = form.cleaned_data['first_name']
                if form.cleaned_data['last_name']:
                    obj.last_name = form.cleaned_data['last_name']
                if form.cleaned_data['occupation']:
                    obj.occupation = form.cleaned_data['occupation']
                if form.cleaned_data['company']:
                    obj.company = form.cleaned_data['company']
                if form.cleaned_data['phone']:
                    obj.phone = form.cleaned_data['phone']
                if form.cleaned_data['email']:
                    obj.email = form.cleaned_data['email']
                if form.cleaned_data['address']:
                    obj.address = form.cleaned_data['address']
                if form.cleaned_data['visit_date']:
                    obj.visit_date = form.cleaned_data['visit_date']
                if form.cleaned_data['visit_hour']:
                    obj.visit_hour = form.cleaned_data['visit_hour']
                if form.cleaned_data['visit_minute']:
                    obj.visit_minute = form.cleaned_data['visit_minute']
                if form.cleaned_data['description']:
                    obj.description = form.cleaned_data['description']
                if form.cleaned_data['file']:
                    obj.file = form.cleaned_data['file']
                obj.save()
        if request.POST.get('submit') == 'sample':
            form = SampleForm(request.POST, request.FILES)
            context.update({'form': form})
            if form.is_valid():
                obj = Sample()
                obj.user = User.objects.get(id=request.user.id)
                if form.cleaned_data['pin']:
                    obj.pin = form.cleaned_data['pin']
                if len(request.POST.getlist('field')) > 0:
                    if len(request.POST.getlist('field')[1]) <= 0:
                        if request.POST.getlist('field')[0] == 'stone_cutting_factory':
                            obj.field = 'کارخانه سنگ بری'
                        if request.POST.getlist('field')[0] == 'export':
                            obj.field = 'صادرات'
                        if request.POST.getlist('field')[0] == 'block_warehouse':
                            obj.field = 'انبار بلوک'
                        if request.POST.getlist('field')[0] == 'internal_sales_of_blocks':
                            obj.field = 'فروش داخلی بلوک'
                    else:
                        obj.field = request.POST.getlist('field')[1]
                if form.cleaned_data['tonnage']:
                    obj.tonnage = form.cleaned_data['tonnage']
                if form.cleaned_data['phone']:
                    obj.phone = form.cleaned_data['phone']
                if form.cleaned_data['email']:
                    obj.email = form.cleaned_data['email']
                if form.cleaned_data['male']:
                    if form.cleaned_data['male'] == 'true':
                        obj.male = True
                    else:
                        obj.male = False
                if form.cleaned_data['first_name']:
                    obj.first_name = form.cleaned_data['first_name']
                if form.cleaned_data['last_name']:
                    obj.last_name = form.cleaned_data['last_name']
                if form.cleaned_data['description']:
                    obj.description = form.cleaned_data['description']
                if form.cleaned_data['file']:
                    obj.file = form.cleaned_data['file']
                obj.save()
    return render(request, "product/product_detail_lined.html", context)


class InternalProductCreateView(View):

    def get(self, request):
        return render(request, "product/add_internal.html")

    def post(self, request):
        internal_resource = Internal_Product_Resource()
        dataset = Dataset()
        new_internal = request.FILES['file']
        imported_data = dataset.load(new_internal.read(), format='xlsx')
        result = internal_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            internal_resource.import_data(dataset, dry_run=False)

        return render(request, "product/add_internal.html")


def InternalImage(request):
    if request.method == "POST":
        form = InternalFileLogoForm(request.POST, request.FILES)
        if form.is_valid():
            file = InternalMainPicFile(file=form.cleaned_data["file"])
            file.save()
            return redirect("config:panel_home")


# Exportal
class ExportalProductPanelList(LoginRequiredMixin, ListView):
    model = ExportalProduct
    template_name = "product/exportal_list_panel.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super(ExportalProductPanelList, self).get_context_data(*args, **kwargs)
        context_data["total"] = ExportalProduct.objects.all().count()
        context_data["tonajze"] = ExportalProduct.objects.aggregate(Sum("approximate_tonnage"))[
            'approximate_tonnage__sum']
        return context_data


class ExportalProductListView(LoginRequiredMixin, ListView):
    queryset = ExportalProduct.objects.filter(active=True)[:20]
    template_name = "product/exportal_list.html"


class ExportalProductListCompleteView(LoginRequiredMixin, ListView):
    model = ExportalProduct
    template_name = "product/exportal_list_complete.html"


class ExportalProductCreateView(View):

    def get(self, request):
        return render(request, "product/add_exportal.html")

    def post(self, request):
        internal_resource = Exportal_Product_Resource()
        dataset = Dataset()
        new_exportal = request.FILES['file']
        imported_data = dataset.load(new_exportal.read(), format='xlsx')
        result = internal_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            internal_resource.import_data(dataset, dry_run=False)

        return render(request, "product/add_exportal.html")


def PartialPictureInternalCreateView(request):
    if request.method == "POST":
        form = InternalFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = InternalGalleriesFile(file=form.cleaned_data["file"])
            file.save()
            return redirect("config:panel_home")


# Lined
class LinedProductList(ListView):
    model = LinedProducts
    template_name = "product/line_list.html"


class LinedProductPanelList(ListView):
    model = LinedProducts
    template_name = "product/line_list.html"


# REJECTED

# class RejectedProductList(ListView):
#     model = Rejected
#     template_name = "product/rejected_list_panel.html"
class RejectedProductList(View):
    def get(self, request):
        queryset = RejectedFilter(request.GET, queryset=Rejected.objects.all())
        return render(request, "product/rejected_list_panel.html", {'filter': queryset})


# Loaded


class LoadedProductList(ListView):
    model = Loaded
    template_name = "product/loaded_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super(LoadedProductList, self).get_context_data(*args, **kwargs)
        # context_data["total"]=Loaded.objects.all().count()
        # context_data["tonajze"]=Loaded.objects.aggregate(Sum("weight_of_scales"))
        return context_data


def rejected_update(request):
    return render(request, 'product/rejected_update.html')


def rejected_upload(request):
    if request.method == 'POST':
        rejected_resource = Rejected_Product_Resource()
        dataset = Dataset()
        new_rejected = request.FILES['rejectedData']
        imported_data = dataset.load(new_rejected.read())
        result = rejected_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            rejected_resource.import_data(dataset, dry_run=False)
            for data in imported_data:
                try:
                    if data[7][0] == 'E':
                        obj = ExportalProduct.objects.get(serial_number_of_the_peak_in_the_mine=data[7][0])
                        obj.active = True
                        obj.rejected = True
                        obj.save()
                    elif data[7][0] == 'D':
                        obj = InternalProduct.objects.get(serial_number_of_the_peak_in_the_mine=data[7][0])
                        obj.active = True
                        obj.rejected = True
                        obj.save()
                    elif data[7][0] == 'L':
                        obj = LinedProducts.objects.get(serial_number_of_the_peak_in_the_mine=data[7][0])
                        obj.active = True
                        obj.rejected = True
                        obj.save()
                except:
                    continue
        return redirect("config:panel_home")


def LoadedProductCreateView(request):
    if request.method == 'POST':
        loaded_resource = Loaded_Product_Resource()
        dataset = Dataset()
        new_loaded = request.FILES['loadedData']
        imported_data = dataset.load(new_loaded.read(), format='xlsx')
        result = loaded_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            loaded_resource.import_data(dataset, dry_run=False)  # Actually import now
            for data in imported_data:
                try:
                    if data[7][0] == 'E':
                        obj = ExportalProduct.objects.get(serial_number_of_the_peak_in_the_mine=data[7][0])
                        obj.active = False
                        obj.loaded = True
                        obj.save()
                    elif data[7][0] == 'D':
                        obj = InternalProduct.objects.get(serial_number_of_the_peak_in_the_mine=data[7][0])
                        obj.active = False
                        obj.loaded = True
                        obj.save()
                    elif data[7][0] == 'L':
                        obj = LinedProducts.objects.get(serial_number_of_the_peak_in_the_mine=data[7][0])
                        obj.active = False
                        obj.loaded = True
                        obj.save()
                except:
                    continue
        return redirect("config:panel_home")


class ProductionReportsList(View):
    def get(self, request):
        queryset = ProductFilter(request.GET, queryset=ProductBase.objects.all())
        return render(request, 'product/production_reports.html', {'filter': queryset})


class LoadedReports(View):
    def get(self, request):
        queryset = LoadedFilter(request.GET, queryset=Loaded.objects.all())
        return render(request, 'product/loaded_reports.html', {'filter': queryset})


class DomesticInventory(View):
    def get(self, request):
        queryset = DomesticFilter(request.GET, queryset=InternalProduct.objects.all())
        return render(request, 'product/internal_reports.html', {'filter': queryset})


class ExportalInventory(View):
    def get(self, request):
        queryset = ExportalFilter(request.GET, queryset=ExportalProduct.objects.all())
        return render(request, 'product/exportal_reports.html', {'filter': queryset})


def is_valid_queryparam(param):
    return param != '' and param is not None


def SearchView(request):
    context = {}
    stone_type = request.GET.get('stone_type')
    stone_name = request.GET.get('stone_name')
    mine = request.GET.get('mine')
    color_code = request.GET.get('color_code')

    length_min = request.GET.get('length_min')
    length_max = request.GET.get('length_max')
    height_min = request.GET.get('height_min')
    height_max = request.GET.get('height_max')
    ton = request.GET.get('ton')

    grading_code = request.GET.get('grading_code')
    width_min = request.GET.get("width_min")
    param = False

    queryset = InternalProduct.objects.filter(active=True)
    if is_valid_queryparam(stone_type):
        queryset = queryset.filter(mine__stone_type=stone_type)
        param = True
    if is_valid_queryparam(stone_name):
        queryset = queryset.filter(stone_name=stone_name)
        param = True
    if is_valid_queryparam(mine):
        queryset = queryset.filter(mine__name=mine)
        param = True
    if is_valid_queryparam(grading_code):
        queryset = queryset.filter(grading_code=grading_code)
        param = True
    if is_valid_queryparam(length_max):
        queryset = queryset.filter(length__lte=length_max)
        param = True
    if is_valid_queryparam(length_min):
        queryset = queryset.filter(height__gte=length_min)
        param = True
    if is_valid_queryparam(height_max):
        queryset = queryset.filter(height__lte=height_max)
        param = True
    if is_valid_queryparam(height_min):
        queryset = queryset.filter(height__gte=height_min)
        param = True
    if is_valid_queryparam(width_min):
        queryset = queryset.filter(width__gt=width_min)
        param = True
    if is_valid_queryparam(ton):
        queryset = queryset.filter(approximate_tonnage__gt=ton)
        param = True

    if param:
        internal_product = queryset
    else:
        internal_product = None
    context.update({"internal": internal_product})
    param = False

    queryset = ExportalProduct.objects.filter(active=True)
    if is_valid_queryparam(stone_type):
        queryset = queryset.filter(mine__stone_type=stone_type)
        param = True
    if is_valid_queryparam(stone_name):
        queryset = queryset.filter(stone_name=stone_name)
        param = True
    if is_valid_queryparam(mine):
        queryset = queryset.filter(mine__name=mine)
        param = True
    if is_valid_queryparam(grading_code):
        queryset = queryset.filter(grading_code=grading_code)
        param = True
    if is_valid_queryparam(length_max):
        queryset = queryset.filter(length__lte=length_max)
        param = True
    if is_valid_queryparam(length_min):
        queryset = queryset.filter(height__gte=length_min)
        param = True
    if is_valid_queryparam(height_max):
        queryset = queryset.filter(height__lte=height_max)
        param = True
    if is_valid_queryparam(height_min):
        queryset = queryset.filter(height__gte=height_min)
        param = True
    if is_valid_queryparam(width_min):
        queryset = queryset.filter(width__gt=width_min)
        param = True
    if is_valid_queryparam(ton):
        queryset = queryset.filter(approximate_tonnage__gt=ton)
        param = True
    if is_valid_queryparam(color_code):
        queryset = queryset.filter(color_code=color_code)
        param = True

    if param:
        exportal_product = queryset
    else:
        exportal_product = None
    context.update({"exportal": exportal_product})
    param = False

    queryset = LinedProducts.objects.all()
    if is_valid_queryparam(stone_type):
        queryset = queryset.filter(mine__stone_type=stone_type)
        param = True
    if is_valid_queryparam(stone_name):
        queryset = queryset.filter(stone_name=stone_name)
        param = True
    if is_valid_queryparam(mine):
        queryset = queryset.filter(mine__name=mine)
        param = True
    if is_valid_queryparam(grading_code):
        queryset = queryset.filter(grading_code=grading_code)
        param = True
    if is_valid_queryparam(length_max):
        queryset = queryset.filter(length__lte=length_max)
        param = True
    if is_valid_queryparam(length_min):
        queryset = queryset.filter(height__gte=length_min)
        param = True
    if is_valid_queryparam(height_max):
        queryset = queryset.filter(height__lte=height_max)
        param = True
    if is_valid_queryparam(height_min):
        queryset = queryset.filter(height__gte=height_min)
        param = True
    if is_valid_queryparam(width_min):
        queryset = queryset.filter(width__gt=width_min)
        param = True
    if is_valid_queryparam(ton):
        queryset = queryset.filter(approximate_tonnage__gt=ton)
        param = True
    if is_valid_queryparam(color_code):
        queryset = queryset.filter(color_code=color_code)
        param = True

    if param:
        lined_product = queryset
    else:
        lined_product = None
    context.update({"lined": lined_product})

    return render(request, "product/search.html", context)
