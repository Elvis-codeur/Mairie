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


def save_journal(a,acte,type):
    print(a)

    ac = acte
    if(type == "mariage"):
        ac = ActesMariageModel()
    elif(type == "naissance"):
        ac = ActesNaissanceModel()
    else:
        ac = ActesDecesModel()

    print("j = ",ac)
    
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
    