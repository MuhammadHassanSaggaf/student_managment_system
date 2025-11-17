# accounts/urls.py
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("create/", views.account_create, name="account_create"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("list/", views.account_list, name="account_list"),
    path("student/<str:admission_number>/", views.account_detail_by_admission, name="account_detail"),
]
