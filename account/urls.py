from django.urls import path
from .views import LoginView, UserLogout, SpecialUserList, PotentialUserList, PossibleUserList, SpecialUserCreateView, \
    FavoriteProduct, GetPassword, AdminUserList, ActivityListView, AdminCreateView, SiteActivityListView,Create_favorite,UserInfo

app_name = "account"
urlpatterns = [
    path("profile/",UserInfo.as_view(),name="profile"),
    path("", LoginView, name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("special_user/", SpecialUserList.as_view(), name="special_user"),
    path("potential_user/", PotentialUserList.as_view(), name="potential_user"),
    path("possible_user/", PossibleUserList.as_view(), name="possible_user"),
    path("special_user_list/", SpecialUserCreateView.as_view(), name="special_user_create"),
    path("favorite_product/", FavoriteProduct.as_view(), name="favorite_product"),
    path("get_password/", GetPassword.as_view(), name="get_password"),
    path("Activity_list/", ActivityListView.as_view(), name="activity_list"),
    path("admin_list/", AdminUserList.as_view(), name="admin_list"),
    path("admin_create/", AdminCreateView.as_view(), name="admin_create"),
    path("site_activity/", SiteActivityListView.as_view(), name="site_activity"),
    path("create_favorite/<unique_id>/",Create_favorite,name="create_favorite")

]
