from django.db import models
from django.forms.models import model_to_dict



class ActesNaissanceModel(models.Model):

   le = models.CharField(verbose_name= "Le",max_length=300)
   heure = models.IntegerField(verbose_name="heure(s)")
   minutes = models.IntegerField(verbose_name="minute(s)")

   est_ne_ville = models.CharField(verbose_name="est né à (Ville)",max_length=25)
   est_ne_pays = models.CharField(verbose_name= "(Pays)",max_length=25)

   nom = models.CharField(verbose_name="Nom",max_length=25)
   prenom = models.CharField(verbose_name="Prénom(s)",max_length=100)
   sexe = models.CharField(verbose_name="sexe",max_length=15)

   parent_1 = models.CharField(verbose_name=  "Fils (e) de (Père)",max_length=50)
   parent_1_naissance_date = models.CharField(verbose_name= "Date de naissance du père",max_length=30)

   parent_1_naissance_lieu = models.CharField(verbose_name="Lieu de naissance du père",max_length=40)

   parent_1_profession = models.CharField(verbose_name= "Profession du père",max_length=20)

   parent_1_domicile = models.CharField(verbose_name="Domicile du père",max_length=50)


   #Mère
   parent_2 = models.CharField(verbose_name=  "Fils (e) de (Mère)",max_length=50)
   parent_2_naissance_date = models.CharField(verbose_name= "Date de naissance de la mère",max_length=30)

   parent_2_naissance_lieu = models.CharField(verbose_name="Lieu de naissance de la mère",max_length=40)

   parent_2_profession = models.CharField(verbose_name= "Profession de la mère",max_length=20)

   parent_2_domicile = models.CharField(verbose_name="Domicile de la mère",max_length=30)


   dresse_le = models.CharField(verbose_name="Dressé le",max_length=100)

   dresse_le_heure = models.IntegerField(verbose_name="Dressé le (minutes)")
   dresse_le_minutes = models.IntegerField(verbose_name="Dressé le (minutes)")
   dresse_le_decla = models.CharField(verbose_name="sur la déclaration de",max_length=200)
   dresse_le_age= models.IntegerField(verbose_name="Dressé âges")
   dresse_domicile= models.CharField(verbose_name="Dressé domicile",max_length=30)
   dresse_lecture= models.CharField(verbose_name="avec Nous",max_length=200)