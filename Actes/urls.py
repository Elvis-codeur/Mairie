from django.urls import path,include 
import  Actes.views as views  

urlpatterns = [
    
    path('actes/l', views.p,name = "p"),
    path("actes/d",views.actes_deces_form,name = ""),

    path("actes/k",views.index,name = "index"),
    path("actes/m",views.actes_mariage_form,name =""),
    path("actes/ds",views.serve_acte_dece,name=""),
    path("actes/u",views.i,name=""),
    

]