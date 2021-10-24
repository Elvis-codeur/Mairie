from django.urls import path
import  Client.views as views  

from .links import LINKS

urlpatterns = [
    path(LINKS["dashboard"][0],views.dashboard,name ="dashboard"),
    path(LINKS["add-naissance"][0],views.add_naissance,name = "naissance"),
    path(LINKS["add-deces"][0],views.add_deces,name = "deces"),
    path(LINKS["add-mariage"][0],views.add_mariage,name = "mariage"),
]