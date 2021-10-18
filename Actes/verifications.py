from django import template
from django.template import context, loader
from Actes.forms import *
from Actes.models import *

def generate_actes_naissance(dic_):
    """
    Cette méthode génère les actes de naissances à l'enrégistrement
    """
    template = loader.get_template("Actes/generer_acte_naissance.html")
    form = ActesNaissanceForm(auto_id=True)
    l =[]
    compteur = 0
    dic_keys = list(dic_.keys())
    print(dic_)

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
    

def save_acte_naissance(dic):
    a = "from Actes.models import ActesNaissanceModel\na = ActesNaissanceModel()\n"

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

    """
    result = False
    try:
        
    except Exception as e:
        print(e)

    return result
    """



"""c = compile(code,"fill_débug.txt","exec")
            result =  0
            try:
                result = exec(c)
                print("yes")"""
