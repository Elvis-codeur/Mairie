from django.db import close_old_connections
from django.forms.forms import Form
from django.http.response import HttpResponse

from Client.forms import MaireLoginForm

from .links import LINKS

from django.conf import settings
from Client.models import *

from django.urls import reverse

def create_url_message(tab,action):
    return "mairie={} maire={} executant={} action={}".format(tab[0],tab[1],tab[2],action)

def create_message(user):

    identifiant =0

    maire_identifiant = 0
    officier_identifiant = 0
    mairie_identifiant = 0

    maire = False
    officier = False

    try:
        identifiant = get_maireid_by_user(user)
        maire = True
    except:
        identifiant = get_officierid_by_user(user)
        officier = True

    if(maire):
        maire_identifiant = identifiant
    else:
        officier_identifiant = identifiant
        officier = get_executant_by_id(identifiant)
        maire_identifiant = officier.maire.identifiant
        mairie_identifiant = officier.mairie.identifiant

    return mairie_identifiant,maire_identifiant,officier_identifiant


def create_links(langue,request = ""):
    l = {}
    preffix =["n","d","m"]

    mairie_identifiant,maire_identifiant,officier_identifiant = create_message(request.user)
    for i,u in zip(list(LINKS.keys())[1:],preffix):
        l["{}".format(u)] = "/"+langue+"/"+settings.CLIENT_URL+LINKS[i][1]+ \
        create_url_message([mairie_identifiant,officier_identifiant,maire_identifiant],"create")

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


def modify_message(message,keyword,value):
    a = parse_message(message)
    a[keyword] = value

    b = ""
    for i in a.keys():
        b = b+"{}={} ".format(i,a[i])

    return b


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
            a = reverse("Client:officier_naissance_vue",
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
            a = reverse("Client:officier_deces_vue",
                kwargs={"message":messsage + " deces={}".format(i.identifiant)})

            p["link"]= a
            p['nom'] = i.nom
            p["prenom"] = i.prenom
            p["le"] = i.le 
            l.append(p)

    elif(classname == "mariage"):
        tab = ActesMariageModel.objects.all()
        for i in tab:
            p = {}
            a = reverse("Client:officier_mariage_vue",
                kwargs={"message":messsage + " mariage={}".format(i.identifiant)})

            p["link"]= a
            p['nom'] = i.nom1
            p["prenom"] = i.nom2
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


def prepare_input(input,model,i):
    a = input.as_text()
    b = a.split(" ")
    key = model.keys()
    #rom = list(key)
    r = ''
    if(type(model[rom[i]]) == type(str)):
        r = model[rom[i]]
    else:
        r = ""
    return b[:1]+[r]+b[1:]
    
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


from django import template
from django.template import context, loader
from Actes.forms import *
from Actes.models import *

import pdfkit
import random

def generate_actes_deces(dic_):
    """
    Cette méthode génère les actes de naissances à l'enrégistrement
    """
    template = loader.get_template("Actes/generer_acte_naissance.html")
    form = ActesDecesForm(auto_id=True)
    l =[]
    compteur = 0
    dic_keys = list(dic_.keys())
    #print(dic_)

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
    return template.render(context = context)
 
def generate_actes_naissance(dic_):
    """
    Cette méthode génère les actes de décès à l'enrégistrement
    """
    template = loader.get_template("Actes/generer_acte_naissance.html")
    form = ActesNaissanceForm(auto_id=True)
    l =[]
    compteur = 0
    dic_keys = list(dic_.keys())
    #print(dic_)

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
    return template.render(context)
    

def save_acte_naissance(dic,modify=False,message = ""):
    ident = generate_id(ActesNaissanceModel)
    

    a = ""
    if not modify:
        a = "from Actes.models import ActesNaissanceModel\na = ActesNaissanceModel()\n"
        a = a+ "a.identifiant = ident\n"
    else:
        me = parse_message(message)
        ident = me["naissance"]
        a = a+ 'a = get_actesnaissance_by_id(me["naissance"])\n'

    #a = a + str(dic)+"\n"
    image = dic["transcription"]
    image1 = dic["original"]

    # On génère le code qu'on va exécuter
    keys = list(dic.keys())
    for i in keys[:len(keys)-1]:

        if(type(1) == type(dic[i])):
            a = a+"""a.{}={}\n""".format(i,dic[i])
        else:
            a = a+"""a.{}="{}"\n""".format(i,dic[i])

    a = a + "a.trancription=image\n"
    a = a + "a.original = image1\n"
    a = a+"a.save()\n"

    #print(a)
    #On compile et on exécute
    c = compile(a,"fill_débug.txt","exec")
    result = exec(c)
    return ident

def save_acte_deces(dic,modify=False,message = ""):
    ident = generate_id(ActesDecesModel)
    

    a = ""
    if not modify:
        a = "from Actes.models import ActesDecesModel\na = ActesDecesModel()\n"
        a = a+ "a.identifiant = ident\n"
    else:
        me = parse_message(message)
        ident = me["naissance"]
        a = a+ 'a = get_actesdeces_by_id(me["naissance"])\n'   
    #a = a + str(dic)+"\n"
    image = dic["transcription"]
    image1 = dic["original"]

    # On génère le code qu'on va exécuter
    keys = list(dic.keys())
    for i in keys[:len(keys)-1]:

        if(type(1) == type(dic[i])):
            a = a+"""a.{}={}\n""".format(i,dic[i])
        else:
            a = a+"""a.{}="{}"\n""".format(i,dic[i])

    a = a + "a.trancription=image\n"
    a = a + "a.original = image1\n"
    a = a+"a.save()\n"

    #print(a)
    #On compile et on exécute
    c = compile(a,"fill_débug.txt","exec")
    result = exec(c)
    return ident

def save_actes_mairiage(dic,modify=False,message = ""):
    ident = generate_id(ActesMariageModel)
    a = ""
    if not modify:
        a = "from Actes.models import ActesMariageModel\na = ActesMariageModel()\n"
        a = a+ "a.identifiant = ident\n"
    else:
        me = parse_message(message)
        ident = me["naissance"]
        a = a+ 'a = get_actesmariage_by_id(me["naissance"])\n'

    image = dic["transcription"]
    image1 = dic["original"]

    # On génère le code qu'on va exécuter
    keys = list(dic.keys())
    for i in keys[:len(keys)-1]:

        if(type(1) == type(dic[i])):
            a = a+"""a.{}={}\n""".format(i,dic[i])
        else:
            a = a+"""a.{}="{}"\n""".format(i,dic[i])

    a = a + "a.trancription=image\n"
    a = a + "a.original = image1\n"
    a = a+"a.save()\n"

    #print(a)
    #On compile et on exécute
    c = compile(a,"fill_débug.txt","exec")
    result = exec(c)
    return ident


def generate_acte_naissance_fromdb(message):
    form = ActesNaissanceForm(auto_id=True)
    me = parse_message(message)
    naissance = get_actesnaissance_by_id(me["naissance"])
    dic_ = naissance.__dict__
    # On prend les différens labels
    form_list  = [i.label for i in form]
    model_list = []
    
    # On récupère seleument les infos utiles des db
    for i in list(dic_.keys())[7:len(dic_.keys())-1]:
        model_list.append(i)

    compteur = 0
    l = []
    print(model_list)
    # On laisse les images pour un traitement spécial
    for i in list(form)[5:]:
        if(compteur<25):

            dic = {}
            dic["f"]= " : "+str(dic_[model_list[compteur]])
            dic["label"] = i.label
            dic["label_value"] = dic_[model_list[compteur]]
            a = str(i)
            a = a.split(" ")
            for kl in a:
                if("containner" in kl):
                    c = kl.split("=")[1]
                    dic["containner"] = c[1:len(c)-1]
                
            #print(dic)
            l.append(dic)
            compteur += 1

        else:
            break

        #dic = {}
        #dic["f"] = '<a href = "{}" > </a>'.format(naissance.original.url)
        #dic["label"] = "Original"
        #dic["label_value"] = str(naissance.original.url)

    return l


def generate_acte_deces_fromdb(message):
    form = ActesDecesForm(auto_id=True)
    me = parse_message(message)
    deces = get_actesdeces_by_id(me["deces"])
    dic_ = deces.__dict__
    # On prend les différens labels
    form_list  = [i.label for i in form]
    model_list = []
    
    # On récupère seleument les infos utiles des db
    for i in list(dic_.keys())[7:len(dic_.keys())-1]:
        model_list.append(i)

    compteur = 0
    l = []
    #print(len(form_list),"\n\n")
    #print(len(model_list))
    
    
    # On laisse les images pour un traitement spécial
    for i in list(form)[5:]:
        if(compteur<25):

            dic = {}
            dic["f"]= " : "+str(dic_[model_list[compteur]])
            dic["label"] = i.label
            dic["label_value"] = dic_[model_list[compteur]]
            a = str(i)
            a = a.split(" ")
            for kl in a:
                if("containner" in kl):
                    c = kl.split("=")[1]
                    dic["containner"] = c[1:len(c)-1]
                
            #print(dic)
            l.append(dic)
            compteur += 1

        else:
            break

        #dic = {}
        #dic["f"] = '<a href = "{}" > </a>'.format(naissance.original.url)
        #dic["label"] = "Original"
        #dic["label_value"] = str(naissance.original.url)
        
    return l

def generate_acte_mariage_fromdb(message):
    form = ActesMariageForm(auto_id=True)
    me = parse_message(message)
    deces = get_actesmariage_by_id(me["mariage"])
    dic_ = deces.__dict__
    # On prend les différens labels
    form_list  = [i.label for i in form]
    model_list = []
    
    # On récupère seleument les infos utiles des db
    for i in list(dic_.keys())[7:len(dic_.keys())-1]:
        model_list.append(i)

    compteur = 0
    l = []
    #print(form_list,"\n\n")
    #print(model_list)
    
    
    # On laisse les images pour un traitement spécial
    for i in list(form)[5:]:
        if(compteur<25):

            dic = {}
            dic["f"]= str(dic_[model_list[compteur]])
            dic["label"] = i.label
            dic["label_value"] = dic_[model_list[compteur]]
            a = str(i)
            a = a.split(" ")
            for kl in a:
                if("containner" in kl):
                    c = kl.split("=")[1]
                    dic["containner"] = c[1:len(c)-1]
                
            #print(dic)
            l.append(dic)
            compteur += 1

        else:
            break

        #dic = {}
        #dic["f"] = '<a href = "{}" > </a>'.format(naissance.original.url)
        #dic["label"] = "Original"
        #dic["label_value"] = str(naissance.original.url)
        
    return l


def get_maireid_by_user(username):
    user = User.objects.get(username= username)
    return Maire.objects.get(user = user).identifiant

def get_officierid_by_user(username):
    user = User.objects.get(username= username)
    return Executant.objects.get(user = user).identifiant

def generate_id(model):
    z = model.objects.all()
    if(len(z) == 0):
         return random.randint(2**4,10**9)
    else:
        ok = True
        result = 0
        while(ok):
            result = random.randint(2**4,10**9)
            ident = [i.identifiant for i in z]
            if(result in ident):
                ok = True
            else:
                ok = False

        return result


