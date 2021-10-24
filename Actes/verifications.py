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
    print(template.render(context))
    return pdfkit.from_url()
    

def save_acte_naissance(dic):
    ident = generate_id(ActesNaissanceModel)
    a = "from Actes.models import ActesNaissanceModel\na = ActesNaissanceModel()\n"
    a = a+ "a.identifiant = ident\n"
    #a = a + str(dic)+"\n"
    image = dic["scan_manuscrit"]

    # On génère le code qu'on va exécuter
    keys = list(dic.keys())
    for i in keys[:len(keys)-1]:

        if(type(1) == type(dic[i])):
            a = a+"""a.{}={}\n""".format(i,dic[i])
        else:
            a = a+"""a.{}="{}"\n""".format(i,dic[i])

    a = a + "a.scan_manuscrit=image\n"
    a = a+"a.save()\n"

    #print(a)
    #On compile et on exécute
    c = compile(a,"fill_débug.txt","exec")
    result = exec(c)
    return ident

def save_acte_deces(dic):
    ident = generate_id(ActesDecesModel)
    a = "from Actes.models import ActesDecesModel\na = ActesDecesModel()\n"
    a = a + "a.identifiant = ident\n"      
    #a = a + str(dic)+"\n"
    image = dic["scan_manuscrit"]

    # On génère le code qu'on va exécuter
    keys = list(dic.keys())
    for i in keys[:len(keys)-1]:

        if(type(1) == type(dic[i])):
            a = a+"""a.{}={}\n""".format(i,dic[i])
        else:
            a = a+"""a.{}="{}"\n""".format(i,dic[i])

    a = a + "a.scan_manuscrit=image\n"
    a = a+"a.save()\n"

    #print(a)
    #On compile et on exécute
    c = compile(a,"fill_débug.txt","exec")
    result = exec(c)
    return ident

def save_actes_mairiage(dic):
    ident = generate_id(ActesMariageModel)
    a = "from Actes.models import ActesMariageModel\na = ActesMariageModel()\n"
    a = a + "a.identifiant = ident\n"      
    #a = a + str(dic)+"\n"
    image = dic["scan_manuscrit"]

    # On génère le code qu'on va exécuter
    keys = list(dic.keys())
    for i in keys[:len(keys)-1]:

        if(type(1) == type(dic[i])):
            a = a+"""a.{}={}\n""".format(i,dic[i])
        else:
            a = a+"""a.{}="{}"\n""".format(i,dic[i])

    a = a + "a.scan_manuscrit=image\n"
    a = a+"a.save()\n"

    #print(a)
    #On compile et on exécute
    c = compile(a,"fill_débug.txt","exec")
    result = exec(c)
    return ident


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


