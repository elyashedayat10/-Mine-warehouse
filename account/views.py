from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Favorite, Activity, SiteActivity
from django.views.generic import View, ListView, CreateView
from .forms import LoginForm, SpecialUserForm, AdminUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminUserMixin
from django.urls import reverse_lazy
from product.models import ProductBase,InternalProduct,ExportalProduct


# Create your views here.
def LoginView(request):
    form_class = LoginForm
    template_name = "account/login.html"
    if request.method == "POST":
        cd = request.POST
        user = authenticate(request, email=cd["email"], password=cd["password"])
        if user is not None:
            login(request, user)
            return redirect("config:site_home")
        else:
            return redirect("/")
    return render(request, "account/login.html")
    # # def dispatch(self, request, *args, **kwargs):
    # #     if request.user.is_authenticated:
    # #         return redirect("config:site_home")
    #
    # def get(self, request):
    #     return render(request, self.template_name, {"from": self.form_class})
    #
    # def post(self, request):
    #         cd = request.POST
    #         user = authenticate(request, email=cd["email"], password=cd["password"])
    #         if user is not None:
    #             login(request, user)
    #             return redirect("config:site_home")
    #         else:
    #             return redirect("/")
    #     return render(request, self.template_name, {"form": form})


class GetPassword(View):
    form_class = LoginForm
    template_name = "account/get_password.html"

    # def dispatch(self, request, *args, **kwargs):
    # if request.user.is_authenticated:
    # return redirect("config:site_home")

    def get(self, request):
        return render(request, self.template_name, {"from": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd["email"], password=cd["password"])
            if user is not None:
                login(request, user)
                return redirect("config:site_home")
            else:
                return redirect("/")
        return render(request, self.template_name, {"form": form})


class UserLogout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("account:login")


class SpecialUserList(AdminUserMixin, ListView):
    queryset = User.objects.filter(is_special=True)
    template_name = "account/special_user.html"
    context_object_name = "special_user"


class PotentialUserList(AdminUserMixin, ListView):
    queryset = User.objects.filter(is_potential=True)
    template_name = "account/potential_user.html"


class PossibleUserList(AdminUserMixin, ListView):
    queryset = User.objects.filter(is_possible=True)
    template_name = "account/possible_user.html"


class SpecialUserCreateView(CreateView):
    model = User
    form_class = SpecialUserForm
    success_url = reverse_lazy("config:panel_home")
    template_name = "account/special_user_create.html"

    def form_valid(self, form):
        new = form.save(commit=False)
        new.is_special = True
        new.save()
        return super(SpecialUserCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(SpecialUserCreateView, self).form_invalid(form)


class FavoriteProduct(View):
    def get(self, request):
        item_list = Favorite.objects.filter(user=User.objects.get(id=request.user.id))
        internal_favorite = []
        external_favorite = [] 
        for internal_p in item_list:
            it = InternalProduct.objects.filter(unique_id=internal_p.product.unique_id)
            if it.exists():
                internal_favorite.append(it)
        for exportal_p in item_list:
            iy = ExportalProduct.objects.filter(unique_id=exportal_p.product.unique_id)
            if iy.exists():
                external_favorite.append(iy)
        return render(request, "account/wish_list.html", context={"internal_favorite": internal_favorite, "exportal_favorite": external_favorite})



def Create_favorite(request, unique_id):
    product = get_object_or_404(ProductBase, unique_id=unique_id)
    check=Favorite.objects.filter(user=User.objects.get(id=request.user.id), product=product.id)
    if check.exists():
        return redirect("account:favorite_product")
    else:
        Favorite.objects.create(user=User.objects.get(id=request.user.id), product_id=product.id)
        return redirect("account:favorite_product")


class AdminUserList(ListView):
    queryset = User.objects.filter(is_admin=True)
    template_name = "account/admin_list.html"


class AdminCreateView(CreateView):
    model = User
    form_class = AdminUserForm
    success_url = reverse_lazy("account:admin_list")
    template_name = "account/create_admin.html"

    def form_valid(self, form):
        new = form.save(commit=False)
        new.is_admin = True
        new.save()
        return super(AdminCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(AdminCreateView, self).form_invalid(form)


class ActivityListView(ListView):
    model = Activity
    template_name = "account/admin_activity.html"
    context_object_name = "admin"


class SiteActivityListView(ListView):
    model = SiteActivity
    template_name = "account/site_activity.html"
    
    
class UserInfo(View):
    def get(self,request):
        return render(request,"account/profile.html")
    
    
