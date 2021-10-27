from django.urls import path,re_path
import  Client.views as views  

from .links import LINKS

app_name = "Client"
urlpatterns = [
    path(LINKS["dashboard"][0],views.dashboard,name ="dashboard"),
    path(LINKS["add-naissance"][0],views.add_naissance,name = "naissance"),
    path(LINKS["add-deces"][0],views.add_deces,name = "deces"),
    path(LINKS["add-mariage"][0],views.add_mariage,name = "mariage"),
    path(LINKS["officier-view"][0],views.account_view,name = "officer_account"),

    # POur le maire
    path(LINKS["maire dahboard"][0],views.maire_account_view,name ="maire_account_view"),
    path(LINKS["maire-deces"][0],views.maire_deces_view,name = "maire_dece_view"),
    path(LINKS["maire-naissance"][0],views.maire_naissance_view,name="maire_naissance_view"),
    path(LINKS["maire-mariage"][0],views.maire_mariage_view,name="maire_mariage_view"),

    path(LINKS["modify-naissance"][0],views.modify_naissance,name="modify_naissance"),
    path("get/<str:code>",views.get_element,name = "get_element"),
]