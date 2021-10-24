from django.db import models


class ActesNaissanceModel(models.Model):

   identifiant = models.IntegerField(default=0)


   le = models.CharField(verbose_name= "Le",max_length=300)
   heure = models.IntegerField(verbose_name="heure(s)",default=0)
   minute = models.IntegerField(verbose_name="minute(s)",default=0)

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

   dresse_le_heure = models.IntegerField(verbose_name="Dressé le (minutes)",default=0)
   dresse_le_minutes = models.IntegerField(verbose_name="Dressé le (minutes)",default=0)
   dresse_le_decla = models.CharField(verbose_name="sur la déclaration de",max_length=200)
   dresse_le_age= models.IntegerField(verbose_name="Dressé âges",default=0)
   dresse_domicile= models.CharField(verbose_name="Dressé domicile",max_length=30)
   dresse_lecture= models.CharField(verbose_name="avec Nous",max_length=200)

   scan_manuscrit = models.FileField(upload_to="actes_naissance_original/",default="")

   def __str__(self) :
       return self.nom + " " + self.prenom


class ActesDecesModel(models.Model):
    identifiant = models.IntegerField(default=0)
    # Première parties
    le = models.CharField(verbose_name="Le",max_length=300,default="")
    
    heure = models.IntegerField(verbose_name="Heure(s)",default=0)

    minute = models.IntegerField(verbose_name="minutes(s)",default=0)

    est_mort_ville = models.CharField(verbose_name = "est décédé (e) à (ville)",default="",max_length=30)
   
    est_mort_pays = models.CharField(verbose_name= "(Pays)",default="",max_length=30)
   
    nom = models.CharField(verbose_name="Nom",default="",max_length=20)
    
    prenom = models.CharField(verbose_name = "Prénom(s)",default="",max_length=100)
    
    sexe = models.CharField(verbose_name = "de sexe",default="",max_length=15)
    
    date_naissance = models.CharField(verbose_name= "est né ",default="",max_length=30)
    
    lieu_naissance = models.CharField(verbose_name= "à",default="",max_length=30)
    
    profession = models.CharField(verbose_name= "Profession",default="",max_length=20)
    
    domicile = models.CharField(verbose_name="Domiciliée à",default="",max_length=20)
    
    # Deuxième partie
    parent_1 = models.CharField(verbose_name="Fils (le) de",default="",max_length=100)
    
    parent_2 = models.CharField(verbose_name= "et de",default="",max_length=100)
    

    parent_1_profession = models.CharField(verbose_name="Profession",default="",max_length=20)
    
    parent_1_domicile2 = models.CharField(verbose_name= "Domiciliée à",default="",max_length=100)
    
    parent_2_profession = models.CharField(verbose_name= "Profession",default="",max_length=20)
    
    parent_2_domicile2 = models.CharField(verbose_name= "Domiciliée à",default="",max_length=100)


    dresse_le = models.CharField(verbose_name="Dressé le",max_length=100)

    dresse_le_heure = models.IntegerField(verbose_name="Dressé le (minutes)",default=0)
    dresse_le_minutes = models.IntegerField(verbose_name="Dressé le (minutes)",default=0)
    dresse_le_decla = models.CharField(verbose_name="sur la déclaration de",max_length=200)
    dresse_le_age= models.IntegerField(verbose_name="Dressé âges",default=0)
    dresse_domicile= models.CharField(verbose_name="Dressé domicile",max_length=30)
    dresse_lecture= models.CharField(verbose_name="avec Nous",max_length=200)

    scan_manuscrit = models.FileField(upload_to="actes_deces_original/",default="")

    def __str__(self) :
       return self.nom + " " + self.prenom
    

class ActesMariageModel(models.Model):
    identifiant = models.IntegerField(default=0)
    # Première parties
    le = models.CharField(verbose_name= "Le",default="",max_length=300)
    
    heure = models.IntegerField(verbose_name= "heures(s)",default=0)
    
    minute = models.IntegerField(verbose_name= "minutes(s)",default=0)
    
    sep = models.CharField(verbose_name= "devant NOUS\nOfficier de l'Etat Civil, "
    "ont comparu publiquement dans la commune du Golfe 1  (Lomé-TOGO)", default="",max_length=2)

    
    #Homme
    nom1 = models.CharField(verbose_name= "Nom",default="",max_length=20)
    
    prenom1 = models.CharField(verbose_name= "Prénom(s)",default="",max_length=100)
    
    nationalite1 = models.CharField(verbose_name= "de Nationalité",default="",max_length=25)
    
    ne_le_homme = models.CharField(verbose_name="Date de naissance (Homme)",default="",max_length=30)

    profession1 = models.CharField(verbose_name= "Profession",default="",max_length=20)
    
    domicile1 = models.CharField(verbose_name= "Domicilié à",default="",max_length=20)
    
    homme_parent_1 =  models.CharField(verbose_name= "Fils majeur/mineur de",default="",max_length=100)
    
    homme_parent_2 =  models.CharField(verbose_name= "Et de",default="",max_length=100)
    
    #Femme
    nom2 = models.CharField(verbose_name= "Nom",default="",max_length=20)
    
    prenom2 = models.CharField(verbose_name= "Prénom(s)",default="",max_length=100)
    
    nationalite2 = models.CharField(verbose_name= "de Nationalité",default="",max_length=20)
    
    ne_le_femme = models.CharField(verbose_name="Date de naissance (Femme)",default="",max_length=30)

    profession2 = models.CharField(verbose_name= "Profession",default="",max_length=20)
    
    domicile2 = models.CharField(verbose_name= "Domicilié à",default="",max_length=20)
    
    femme_parent_1 =  models.CharField(verbose_name= "Fils majeur/mineur de",default="",max_length=100)
   
    femme_parent_2 =  models.CharField(verbose_name= "Et de",default="",max_length=100)
    
    contrat_mariage = models.CharField(verbose_name= "Contrat de mariage",default="",max_length=100)
    
    option = models.CharField(verbose_name= "Option",default="",max_length=50)
    
    sep2 = models.CharField(verbose_name= """Les futurs époux décidèrent l'un après l'autre se prendre
    pour époux et nous avons prononcé au nom de la loi qu'ils sont unis par le mariage en 
    présence de """,default="",max_length=2)
    
    present_1 = models.CharField(verbose_name= "1/",default="",max_length=100)
    
    present_2 = models.CharField(verbose_name= "2/",default="",max_length=100)
    

    dresse_lecture= models.CharField(verbose_name= "tous deux témoins majeurs qui lecture faite,"
    " ont signé avec les époux et NOUS",default="",max_length=100)
    
    scan_manuscrit = models.FileField(upload_to="actes_mariage_original/")

    def __str__(self) :
       return self.nom1 + " " + self.prenom1 + "|"+ self.nom2 + " "+ self.prenom2
