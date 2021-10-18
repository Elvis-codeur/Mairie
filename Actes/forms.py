from django.core.files.storage import default_storage
import django.forms
import django.forms as forms
from django.forms import fields
from Actes.models import *



class ActesNaissanceForm(forms.Form):
    le = forms.CharField(label = "Le",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    heure = forms.IntegerField(label = "heures(s)",
    widget=forms.NumberInput(attrs={"class":"form-control","containner":"col-sm-6"}))

    minute = forms.IntegerField(label = "minutes(s)",
    widget=forms.NumberInput(attrs={"class":"form-control","containner":"col-sm-6"}))
    
    est_ne_ville = forms.CharField(label = "est né (e) à (ville)",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-sm-6"}))

    est_ne_pays = forms.CharField(label = "(Pays)",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-sm-6"}))

    nom = forms.CharField(label = "Nom",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    prenom = forms.CharField(label = "Prénom(s)",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    sexe = forms.CharField(label = "de sexe",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    
    # Deuxième partie
    parent_1 = forms.CharField(label = "Fils (le) de",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_1_naissance_date = forms.CharField(label = "né le",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_1_naissance_lieu = forms.CharField(label = "Lieu de naissance",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_1_profession = forms.CharField(label = "Profession",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_1_domicile = forms.CharField(label = "Domicilié à",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))


    #Troisième partie
    parent_2 = forms.CharField(label = "Et de",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_2_naissance_date = forms.CharField(label = "née le",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_2_naissance_lieu = forms.CharField(label = "à",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_2_profession = forms.CharField(label = "Profession",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_2_domicile = forms.CharField(label = "Domiciliée à",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    # Quatrième partie

    dresse_le = forms.CharField(label = "Dressé le",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))
     
    dresse_le_heure = forms.CharField(label = "heure (s)",
    widget=forms.NumberInput(attrs={"class":"form-control","containner":"col-sm-6"}))

    dresse_le_minutes = forms.CharField(label = "minutes (s)",
    widget=forms.NumberInput(attrs={"class":"form-control","containner":"col-sm-6"}))

    dresse_le_decla = forms.CharField(label = "Sur la déclaration de ",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    dresse_le_age= forms.CharField(label = "âgé (e) de",
    widget=forms.NumberInput(attrs={"class":"form-control","containner":"col-12s"}))

    dresse_domicile= forms.CharField(label = "domicilié (e) à",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    dresse_lecture= forms.CharField(label = "qui lecture faite et invité (e) à lire a (ont) signé avec NOUS",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    scan_manuscrit = forms.FileField()