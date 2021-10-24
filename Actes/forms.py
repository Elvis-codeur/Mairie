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



class ActesDecesForm(forms.Form):
    # Première parties
    le = forms.CharField(label = "Le",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    heure = forms.IntegerField(label = "heures(s)",
    widget=forms.NumberInput(attrs={"class":"form-control","containner":"col-sm-6"}))

    minute = forms.IntegerField(label = "minutes(s)",
    widget=forms.NumberInput(attrs={"class":"form-control","containner":"col-sm-6"}))
    
    est_mort_ville = forms.CharField(label = "est décédé (e) à (ville)",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-sm-6"}))

    est_mort_pays = forms.CharField(label = "(Pays)",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-sm-6"}))

    nom = forms.CharField(label = "Nom",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    prenom = forms.CharField(label = "Prénom(s)",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    sexe = forms.CharField(label = "de sexe",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    date_naissance = forms.CharField(label = "est né(e) le ",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    lieu_naissance = forms.CharField(label = "à",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    profession = forms.CharField(label = "Profession",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    domicile = forms.CharField(label = "Domicilié à",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    # Deuxième partie
    parent_1 = forms.CharField(label = "Fils (le) de",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_2 = forms.CharField(label = "et de",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))


    parent_1_profession = forms.CharField(label = "Profession",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_1_domicile2 = forms.CharField(label = "Domicilié à",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_2_profession = forms.CharField(label = "Profession",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    parent_2_domicile2 = forms.CharField(label = "Domiciliée à",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))


    #Dernière partie
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


class ActesMariageForm(forms.Form):
    # Première parties
    le = forms.CharField(label = "Le",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    heure = forms.IntegerField(label = "heures(s)",
    widget=forms.NumberInput(attrs={"class":"form-control","containner":"col-sm-6"}))

    minute = forms.IntegerField(label = "minutes(s)",
    widget=forms.NumberInput(attrs={"class":"form-control","containner":"col-sm-6"}))
    
    sep = forms.CharField(label = "devant NOUS\nOfficier de l'Etat Civil, ont comparu publiquement dans la commune du Golfe 1  (Lomé-TOGO)",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s","type":"hidden","value":""}))

    #Homme
    nom1 = forms.CharField(label = "Nom",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    prenom1 = forms.CharField(label = "Prénom(s)",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    nationalite1 = forms.CharField(label = "de Nationalité",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    ne_le_homme = forms.CharField(label = "né le",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    profession1 = forms.CharField(label = "Profession",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    domicile1 = forms.CharField(label = "Domicilié à",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    homme_parent_1 =  forms.CharField(label = "Fils majeur/mineur de",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    homme_parent_2 =  forms.CharField(label = "Et de",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    #Femme
    nom2 = forms.CharField(label = "Nom",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    prenom2 = forms.CharField(label = "Prénom(s)",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    nationalite2 = forms.CharField(label = "de Nationalité",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    ne_le_femme = forms.CharField(label = "née le",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    profession2 = forms.CharField(label = "Profession",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    domicile2 = forms.CharField(label = "Domicilié à",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    femme_parent_1 =  forms.CharField(label = "Fils majeur/mineur de",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    femme_parent_2 =  forms.CharField(label = "Et de",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    contrat_mariage = forms.CharField(label = "Contrat de mariage",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    option = forms.CharField(label = "Option",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    sep2 = forms.CharField(label = """Les futurs époux décidèrent l'un après l'autre se prendre
    pour époux et nous avons prononcé au nom de la loi qu'ils sont unis par le mariage en 
    présence de """,
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s","type":"hidden","value":""}))

    present_1 = forms.CharField(label = "1/",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    present_2 = forms.CharField(label = "2/",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))


    dresse_lecture= forms.CharField(label = "tous deux témoins majeurs qui lecture faite,"
    " ont signé avec les époux et NOUS",
    widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))

    scan_manuscrit = forms.FileField()
