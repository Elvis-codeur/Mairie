from django.urls import path,include 
import  Actes.views as views  

urlpatterns = [
    path('l', views.p,name = "p"),
    path("k",views.index,name = "index"),
    path("m",views.receive_naissance,name ="receive_naissance"),

]