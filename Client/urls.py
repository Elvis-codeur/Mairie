from django.urls import path,re_path
import  Client.views as views  

from .links import LINKS

app_name = "Client"
urlpatterns = [
    # Pour l'officier
    path(LINKS["dashboard"][0],views.dashboard,name ="dashboard"),
    path(LINKS["add-naissance"][0],views.add_naissance,name = "naissance"),
    path(LINKS["add-deces"][0],views.add_deces,name = "deces"),
    path(LINKS["add-mariage"][0],views.add_mariage,name = "mariage"),
    path(LINKS["officier-view"][0],views.account_view,name = "officer_account"),

    # POur le maire
    path(LINKS["maire dahboard"][0],views.maire_dashboard,name ="maire_account_view"),
    path(LINKS["maire-deces"][0],views.maire_deces_view,name = "maire_dece_view"),
    path(LINKS["maire-naissance"][0],views.maire_naissance_view,name="maire_naissance_view"),
    path(LINKS["maire-mariage"][0],views.maire_mariage_view,name="maire_mariage_view"),
    path(LINKS["maire-compte"][0],views.maire_account_view,name = "maire_account"),
    path(LINKS["maire-add-off"][0],views.maire_add_officier,name = "maire_add_officier"),
    path(LINKS["maire-officer-account"][0],views.maire_officier_account_view,name = "maire_officier_account"),


    # POur modifier
    path(LINKS["modify-naissance"][0],views.modify_naissance,name="modify_naissance"),
    path(LINKS["modify-deces"][0],views.modify_deces,name="modify_deces"),
    path(LINKS["modify-mariage"][0],views.modify_mariage,name="modify_mariage"),

    # Pour voir
    path(LINKS["view-naissance"][0],views.officier_naissance_vue,name = "officier_naissance_vue"),
    path(LINKS["view-deces"][0],views.officier_deces_vue,name = "officier_deces_vue"),
    path(LINKS["view-mariage"][0],views.officier_mariage_vue,name = "officier_mariage_vue"),
    
    # Pour voir les transcription
    path(LINKS["view-naissance-trans"][0],views.officier_naissance_transcription_vue,name = "officier_naissance_transcription_vue"),
    path(LINKS["view-deces-trans"][0],views.officier_deces_transcription_vue,name = "officier_deces_transcription_vue"),
    path(LINKS["view-mariage-trans"][0],views.officier_mariage_transcription_vue,name = "officier_mariage_transcription_vue"),
    

    #Pour imprimer
    path(LINKS["print-naissance"][0],views.print_naissance,name = "print_naissance"),
    path(LINKS["print-deces"][0],views.print_deces,name="print_deces"), 
    path(LINKS["print-mariage"][0],views.print_mariage,name="print_mariage"),

    #Pour imprimer les pdf des originaux
    path(LINKS["print-pdf-naissance"][0],views.print_naissance_pdf,name = "print_naissance_pdf"),
    path(LINKS["print-pdf-deces"][0],views.print_deces_pdf,name="print_deces_pdf"), 
    path(LINKS["print-pdf-mariage"][0],views.print_mariage_pdf,name="print_mariage_pdf"),

    # Pour imprimer les transcriptions
    path(LINKS["print-naissance-trans"][0],views.print_naissance_transcription,name = "print_transcription_naissance"),
    path(LINKS["print-deces-trans"][0],views.print_deces_transcription,name="print_transcription_deces"), 
    path(LINKS["print-mariage-trans"][0],views.print_mariage_transcription,name="print_transcription_mariage"),

    
     # Pour imprimer les pdf des transcriptions
    path(LINKS["print-pdf-naissance-trans"][0],views.print_naissance_transcription_pdf,name = "print_transcription_naissance_pdf"),
    path(LINKS["print-pdf-deces-trans"][0],views.print_deces_transcription_pdf,name="print_transcription_deces_pdf"), 
    path(LINKS["print-pdf-mariage-trans"][0],views.print_mariage_transcription_pdf,name="print_transcription_mariage_pdf"),

    
    # Pour les login
    path(LINKS["conn-maire"][0],views.maire_login,name="connexion_maire"), 
    path(LINKS["conn-officier"][0],views.officier_login,name="connexion_officier"),

    path(LINKS["deconn-maire"][0],views.maire_deconnect,name="deconnexion_maire"), 
    path(LINKS["deconn-officier"][0],views.officier_deconnect,name="deconnexion_officier"),

    
    
    path("get/<str:code>",views.get_element,name = "get_element"),
]