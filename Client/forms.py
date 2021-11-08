from django import forms
from django.forms import widgets


class NumeroField(forms.widgets.TextInput):
   def __init__(self,**kwargs):
       super().__init__(kwargs)


class MaireLoginForm(forms.Form):
   username = forms.CharField(label = "Votre identifiant")
   password = forms.CharField(max_length = 30,min_length=6,
                                    widget=forms.TextInput(attrs={'class': 'w3-input',
                                    "type":"Password"}),required = True,label="Mot de passe")
    
class OfficierLoginForm(forms.Form):
   username = forms.CharField(label = "Votre identifiant")
   password = forms.CharField(max_length = 30,min_length=6,
                                    widget=forms.TextInput(attrs={'class': 'w3-input',
                                    "type":"Password"}),required = True,label="Mot de passe")
    


CATEGORIE_CHOICES =[
    ("1", "Tout"),
    ("2", "Nom"),
    ("3", "Prénom"),
    ("4", "Date de naissance"),
    ("5", "Ville de naissance"),
    ] 
class SearchForm(forms.Form):

    categorie = forms.MultipleChoiceField(choices = CATEGORIE_CHOICES,
                                          label = "Catégorie",
                                          widget=forms.Select(attrs={'class': 'inp',"id":"catego",
                                          "onclick":"change_sous_categorie()"}))
    
ACTES_CHOICES = [
   ("1", "Naissance"),
   ("2", "Mariage"),
   ("3", "Décès"),
]
class ActesChoiceForm(forms.Form):

   categorie = forms.MultipleChoiceField(choices = ACTES_CHOICES,
                                          label = "Actes de ",
                                          widget=forms.Select(attrs={'class': '',"id":"catego",
                                          "onchange":"change()"}))
    

class ExecutantForm(forms.Form):

   nom = forms.CharField(max_length = 30,
                         widget=forms.TextInput(attrs={"class":"form-control",
                         "containner":"col-12s"}))
    
   prenom = forms.CharField(max_length = 30,
                            widget=forms.TextInput(attrs={"class":"form-control",
                            "containner":"col-12s"}))                                 

   pseudo = forms.CharField(max_length = 20,min_length=5,required = True,
                  widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))
    
   sexe = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=[('homme','Homme'),
                 ('femme','Femme'),]
                 
    )
    
   mot_de_passe = forms.CharField(max_length = 30,min_length=6,
                                    widget=forms.TextInput(attrs={"class":"form-control",
                                    "type":"Password","containner":"col-12s"}),required = True)
    
   numero = forms.CharField(max_length = 30,widget=forms.TextInput(attrs={"class":"form-control",
   "containner":"col-12s"}))

   email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control",
   "containner":"col-12s"}))
   

class MaireForm(forms.Form):

   nom = forms.CharField(max_length = 30,
                         widget=forms.TextInput(attrs={"class":"form-control",
                         "containner":"col-12s"}))
    
   prenom = forms.CharField(max_length = 30,
                            widget=forms.TextInput(attrs={"class":"form-control",
                            "containner":"col-12s"}))                                 

   pseudo = forms.CharField(max_length = 20,min_length=5,required = True,
                  widget=forms.TextInput(attrs={"class":"form-control","containner":"col-12s"}))
    
   sexe = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=[('homme','Homme'),
                 ('femme','Femme'),]
                 
    )
    
   mot_de_passe = forms.CharField(max_length = 30,min_length=6,
                                    widget=forms.TextInput(attrs={"class":"form-control",
                                    "type":"Password","containner":"col-12s"}),required = True)
    
   numero = forms.CharField(max_length = 30,widget=NumeroField(attrs={"class":"form-control",
   "containner":"col-12s"}))

   email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control",
   "containner":"col-12s"}))




   