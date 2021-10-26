from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from Actes.models import *


class LoginJournal(models.Model):
    date_first_creation = models.DateTimeField(auto_now_add=True,verbose_name="Date de parution")
    mairie = models.ForeignKey("Mairie",default = 1,verbose_name="mairie",on_delete=models.SET_DEFAULT)
    maire = models.ForeignKey("Maire",default=1,verbose_name="Maire",on_delete=models.SET_DEFAULT)
    executant = models.ForeignKey("Executant",default=1,verbose_name="Executant",on_delete=models.SET_DEFAULT)
    
    login_latitude = models.FloatField(default=0)
    login_longitude = models.FloatField(default=0)

class NaissanceJournal(LoginJournal):
    naissance = models.ForeignKey(ActesNaissanceModel,default=1,verbose_name="ActesNaissanceModel",on_delete=models.SET_DEFAULT)
    action = ""
    

class DecesJournal(LoginJournal):
    deces = models.ForeignKey(ActesDecesModel,default=1,verbose_name="ActesDecesModel",on_delete=models.SET_DEFAULT)
    action = ""

    def save(self, *args, **kwargs):
        super(DecesJournal, self).save(*args, **kwargs)

class MariageJournal(LoginJournal):
    mariage = models.ForeignKey(ActesMariageModel,default=1,verbose_name="ActesMariageModel",on_delete=models.SET_DEFAULT)
    action = ""

    def save(self, *args, **kwargs):
        super(MariageJournal, self).save(*args, **kwargs)
    


class Maire(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_DEFAULT,default = 1)
    date_first_creation = models.DateTimeField(auto_now_add=True,verbose_name="Date de parution")
    date_last_modification = models.DateTimeField(auto_now=True,verbose_name="Date de dernière modification")
    identifiant = models.IntegerField(default=0)
    nom = models.CharField(default="",verbose_name="Nom",max_length=20)
    prenom = models.CharField(default="",verbose_name="Prénom",max_length=100)
    mairie = models.ForeignKey("Mairie",default = 1,verbose_name="mairie",on_delete=models.SET_DEFAULT)
    def __str__(self):
        return self.nom


class Executant(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_DEFAULT,default = 1)
    date_first_creation = models.DateTimeField(auto_now_add=True,verbose_name="Date de parution")
    date_last_modification = models.DateTimeField(auto_now=True,verbose_name="Date de dernière modification")
    identifiant = models.IntegerField(default=0)
    nom = models.CharField(default="",verbose_name="Nom",max_length=20)
    prenom = models.CharField(default="",verbose_name="Prénom",max_length=100)
    mairie = models.ForeignKey("Mairie",default = 0,verbose_name="mairie",on_delete=models.SET_DEFAULT)
    maire = models.ForeignKey("Maire",default=1,verbose_name="Maire",on_delete=models.SET_DEFAULT)
    
    def __str__(self):
        return self.nom
class Mairie(models.Model):
    #user = models.OneToOneField(User, on_delete=models.SET_DEFAULT,default = 1)
    date_first_creation = models.DateTimeField(auto_now_add=True,verbose_name="Date de parution")
    date_last_modification = models.DateTimeField(auto_now=True,verbose_name="Date de dernière modification")
    identifiant = models.IntegerField(default=0)
    nom = models.CharField(default="",verbose_name="Nom",max_length=50)
    addresse = models.CharField(default="",verbose_name="Adresse",max_length=200)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)

    def __str__(self):
        return self.nom

    
# Create your models here.
