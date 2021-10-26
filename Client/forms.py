from django import forms

class Maire(forms.Form):
   identifiant = forms.IntegerField()
   nom = forms.CharField()
   prenom = forms.CharField()


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
    
