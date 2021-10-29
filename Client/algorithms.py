from django.db import close_old_connections
from django.http.response import HttpResponse

from Actes.verifications import generate_id
from .links import LINKS

from django.conf import settings
from Client.models import *

from django.urls import reverse

def create_url_message(tab,action):
    return "mairie={} executant={} maire={} action={}".format(tab[0],tab[1],tab[2],action)

def create_links(langue):
    l = {}
    preffix =["n","d","m"]

    for i,u in zip(list(LINKS.keys())[1:],preffix):
        l["{}".format(u)] = "/"+langue+"/"+settings.CLIENT_URL+LINKS[i][1]+ create_url_message([0,0,0],"create")

    return l        

def dict_from_list(tab):
    r = {}
    for i in tab:
        k = i.split("=")
        r[k[0]] = k[1]
    return r

def parse_message(message):
    a = message.split(" ")
    return dict_from_list(a)

def get_mairie_by_id(id):
    return Mairie.objects.get(identifiant = id)

def get_maire_by_id(id):
    return Maire.objects.get(identifiant = id)

def get_executant_by_id(id):
    return Executant.objects.get(identifiant = id)

def get_actesnaissance_by_id(id):
    return ActesNaissanceModel.objects.get(identifiant = id)

def get_actesdeces_by_id(id):
    return ActesDecesModel.objects.get(identifiant = id)

def get_actesmariage_by_id(id):
    return ActesMariageModel.objects.get(identifiant = id)


def filter_objects(classname,argument):
    #Pour récuperer nos objets
    if(classname == "naissance"):
        print(ActesNaissanceModel.objects.filter(argument))

def prepare_html_list(classname,messsage):
    l=[]
    if(classname == "naissance"):
        tab = ActesNaissanceModel.objects.all()
        for i in tab:
            p = {}
            a = reverse("Client:modify_naissance",
                kwargs={"message":messsage + " naissance={}".format(i.identifiant)})

            p["link"]= a
            p['nom'] = i.nom
            p["prenom"] = i.prenom
            p["le"] = i.le 
            l.append(p)

    elif(classname == "deces"):
        tab = ActesDecesModel.objects.all()
        for i in tab:
            p = {}
            a = reverse("Client:modify_deces",
                kwargs={"message":messsage + " deces={}".format(i.identifiant)})

            p["link"]= a
            p['nom'] = i.nom
            p["prenom"] = i.prenom
            p["le"] = i.le 
            l.append(p)

    elif(classname == "mariage"):
        tab = MariageJournal.objects.all()
        for i in tab:
            p = {}
            a = reverse("Client:modify_mariage",
                kwargs={"message":messsage + " mariage={}".format(i.identifiant)})

            p["link"]= a
            p['nom'] = i.nom
            p["prenom"] = i.prenom
            p["le"] = i.le 
            l.append(p)

    
    return l

def prepare_maire_html_list(classname,ma,message):
    l = []
    m =" ".join(message.split(" ")[1:])

    if(classname == "naissance"):
        tab = NaissanceJournal.objects.filter(maire = get_maire_by_id(ma))
        #print(tab)
        for i in tab:
            p = {}
            p["link"] = reverse("Client:modify_naissance",kwargs ={"message":m})
            p["nom"] = i.naissance.nom
            p["prenom"] = i.naissance.prenom
            p["executant"] = str(i.executant)
            l.append(p)
    elif(classname == "mariage"):
        tab = MariageJournal.objects.filter(maire = get_maire_by_id(ma))
        #print(tab)
        for i in tab:
            p = {}
            p["link"] = reverse("Client:modify_naissance",kwargs ={"message":m})
            p["nom"] = i.naissance.nom
            p["prenom"] = i.naissance.prenom
            p["executant"] = str(i.executant)
            l.append(p)

    elif(classname == "executant"):
        m = parse_message(message)
        tab = Executant.objects.filter(maire = get_maire_by_id(m["maire"]))
        for i in tab:
            p = {}
            #p["link"] = reverse("Client:modify_naissance",kwargs ={"message":m})
            p["nom"] = i.user.first_name
            p["prenom"] = i.user.last_name
            p["executant"] = i.user.email
            p["numero"] = i.numero
            l.append(p)
    else:
        tab = DecesJournal.objects.filter(maire = get_maire_by_id(ma))
        print(tab)
        for i in tab:
            p = {}
            p["link"] = reverse("Client:modify_naissance",kwargs ={"message":m})
            p["nom"] = i.deces.nom
            p["prenom"] = i.deces.prenom
            p["executant"] = str(i.executant)
            l.append(p)

    

    print(l)
    return l


def save_journal(a,type):
    print(a)

    ac = 1
    if(type == "mariage"):
        ac = MariageJournal()
    elif(type == "naissance"):
        ac = NaissanceJournal()
    else:
        ac = DecesJournal()
    
    ac.maire = get_maire_by_id(int(a["maire"]))
    ac.mairie = get_mairie_by_id(int(a["mairie"]))
    ac.executant = get_executant_by_id(int(a["executant"]))
    ac.action = a["action"]

    if(type == "mariage"):
        ac.mariage = get_actesmariage_by_id(a["ident"])
    elif(type == "naissance"):
        ac.naissance = get_actesnaissance_by_id(a["ident"])
    else:
        ac.deces = get_actesdeces_by_id(a["ident"])

    ac.login_latitude = 0
    ac.login_longitude = 0
    ac.save()
    

def generate_compte_view(exectant):
    
    # Provenant de l'user
    info1 = exectant.user.__dict__
    #Les infos complémentaire
    info2 = exectant.__dict__

    d = dict()

    d["Nom d'utilisateur"] = info1["username"]
    d["Prénom"] = info1["first_name"]
    d["Nom"] = info1["last_name"]
    d["Email"] = info1["email"]
    d["Numero"] = info2["numero"]
    d["Identifiant"]= info2["identifiant"]
    d["Grade"] = info2["grade"]
    return d
    
def save_executant(dic,message):
    a = User()
    a.username = dic["pseudo"]
    a.last_name  = dic["nom"]
    a.first_name = dic["prenom"]
    a.email = dic["email"]
    a.set_password(dic["mot_de_passe"])
    a.is_staff = False
    a.is_superuser = False
    a.save()

    b = Executant()
    b.user = a 
    b.numero = dic["numero"]
    b.sexe = dic["sexe"][0]
    b.identifiant = generate_id(Executant)
    b.maire = get_maire_by_id(message["maire"])
    b.mairie = get_mairie_by_id(message["mairie"])
    b.save()


    """
    for i in form:
        dic = {}
        dic["f"]=i.label
        dic["label"] = i.label
        dic["label_value"] = dic_[dic_keys[compteur]]
        a = str(i)
        a = a.split(" ")
        for kl in a:
            if("containner" in kl):
                c = kl.split("=")[1]
                dic["containner"] = c[1:len(c)-1]
                
        #print(dic)
        l.append(dic)
        compteur += 1


    context = {}
    context["form"] = l[:len(l)-1]
    """

def create_col_head(tab):
    l = []
    for i in tab:
        p = {}
        p["value"] = i
        l.append(p)

    return l
