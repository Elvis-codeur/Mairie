from django.db import close_old_connections
from django.http.response import HttpResponse
from .links import LINKS

from django.conf import settings
from Client.models import *

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

def prepare_html_list(classname):
    l=[]
    if(classname == "naissance"):
        tab = ActesNaissanceModel.objects.all()
        for i in tab:
            p = {}
            p['nom'] = i.nom
            p["prenom"] = i.prenom
            p["le"] = i.le 
            l.append(p)
    #print(l)
    return l

def prepare_maire_html_list(classname,ma):
    l = []
    if(classname == "naissance"):
        tab = NaissanceJournal.objects.filter(maire = get_maire_by_id(ma))
        print(tab)
        for i in tab:
            p = {}
            p["nom"] = i.naissance.nom
            p["prenom"] = i.naissance.prenom
            p["exectutant"] = str(i.executant)
            l.append(p)
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
    return d
    
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
