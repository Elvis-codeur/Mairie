from django.http.response import HttpResponse
from django.shortcuts import render

from django.template import loader
from Actes.forms import *
from Actes.verifications import *
from Client.algorithms import create_links, get_actesnaissance_by_id, get_maire_by_id, get_mairie_by_id, parse_message, save_journal
from Client.forms import *
from Client.models import *
# Create your views here.

def dashboard(request,message):
    deces = ActesDecesModel.objects.all()

    deces_class_nom = ActesDecesModel.objects.order_by("-nom")

    context = {}
     
    l = []
    for i in deces:
        p = {}
        p["nom"] = i.nom
        p["prenom"] = i.prenom
        p["le"] = i.le
        l.append(p)
    context["list"] = l
    # Pour la liste principale

    # Recherche par nom
    l = []
    for i in deces_class_nom:
        p = {}
        p["nom"] = i.nom
        l.append(p)

    context["l_nom"] = l
    

    # Prénom
    l = []
    for i in ActesDecesModel.objects.order_by("-prenom"):
        p = {}
        p["nom"] = i.prenom
        l.append(p)
    context["l_prenom"] = l
    
    # Par date de naissance
    l = []
    for i in ActesDecesModel.objects.order_by("-date_naissance"):
        p = {}
        p["nom"] = i.prenom
        l.append(p)
    context["l_dn"] = l

    f = SearchForm()
    f1 = ActesChoiceForm()
    context["form"] =f
    context["form1"] = f1
    context["links"] = create_links(langue="fr")
    template = loader.get_template("Actes/officiers_vue.html")
    return HttpResponse(template.render(context = context,request = request))
    

def add_naissance(request,message):
    if(request.method == "POST"):
        form = ActesNaissanceForm(request.POST,request.FILES)
        #print(request.POST)
        if(form.is_valid()):
            #print(form.cleaned_data)
            i = save_acte_naissance(form.cleaned_data)
            a = parse_message(message)
            a["ident"] = i
            save_journal(a,ActesNaissanceModel(),"naissance")
            


            #return HttpResponse(generate_actes_naissance(form.cleaned_data))
            return HttpResponse("True")
        else:
            print("LOSE")
        return HttpResponse("none")
    else:
        form = ActesNaissanceForm(auto_id=True)
        l =[]
        for i in form:
            dic = {}
            dic["f"]=i
            dic["label"] = i.label
            a = str(i)
            a = a.split(" ")
            for kl in a:
                if("containner" in kl):
                    c = kl.split("=")[1]
                    dic["containner"] = c[1:len(c)-1]
                
            #print(dic)
            l.append(dic)
            
        context = {}
        context["form"] =l
        context["title"] = "Ajouter actes de naissance"
        context["form_title"] = "ACTE DE NAISSANCE"
        template = loader.get_template("Actes/templates2.html")
        return HttpResponse(template.render(context = context,request = request))


def add_deces(request,message):
    if(request.method == "POST"):
        form = ActesDecesForm(request.POST,request.FILES)
        #print(request.POST)
        if(form.is_valid()):
            #print(form.cleaned_data)
            #print(save_acte_naissance(form.cleaned_data))
            i = save_acte_deces(form.cleaned_data)
            a = parse_message(message)
            a["ident"] = i
            save_journal(a,ActesDecesModel(),"deces")
            #ACTES_DECES_STRING = generate_actes_deces(form.cleaned_data)

            #print("\n\n",ACTES_DECES_STRING)

            #pdf = pdfkit.from_url("http://127.0.0.1:8070/actes/ds",output_path=False)

            #response = HttpResponse(bytes(pdf),content_type='application/pdf')
            #response['Content-Disposition'] = 'filename=some_file.pdf'
            return HttpResponse("True")
            

        else:
            print("LOSE")
        return HttpResponse("none")
    else:
        form = ActesDecesForm(auto_id=True)
        l =[]
        for i in form:
            dic = {}
            dic["f"]=i
            dic["label"] = i.label
            a = str(i)
            a = a.split(" ")
            for kl in a:
                if("containner" in kl):
                    c = kl.split("=")[1]
                    dic["containner"] = c[1:len(c)-1]
                
            #print(dic)
            l.append(dic)
            
        context = {}
        context["form"] =l
        context["title"] = "Ajouter actes de décès"
        context["form_title"] = "ACTE DE DECES"
        template = loader.get_template("Actes/templates2.html")
        return HttpResponse(template.render(context = context,request = request))


def add_mariage(request,message):
    if(request.method == "POST"):
        form = ActesMariageForm(request.POST,request.FILES)
        #print(request.POST)
        if(form.is_valid()):
            #print(form.cleaned_data)
            i = save_actes_mairiage(form.cleaned_data)
            a = parse_message(message)
            a["ident"] = i
            save_journal(a,ActesMariageModel(),"mariage")

            #pdf = generate_actes_deces(form.cleaned_data)

            #response = HttpResponse(bytes(pdf),content_type='application/pdf')
            #response['Content-Disposition'] = 'filename=some_file.pdf'
            return HttpResponse("True")
            

        else:
            print("LOSE")
        return HttpResponse("none")
    else:
        form = ActesMariageForm(auto_id=True)
        l =[]
        for i in form:
            dic = {}
            dic["f"]=i
            dic["label"] = i.label
            a = str(i)
            a = a.split(" ")
            for kl in a:
                if("containner" in kl):
                    c = kl.split("=")[1]
                    dic["containner"] = c[1:len(c)-1]
                
            #print(dic)
            l.append(dic)
            
        context = {}
        context["form"] =l
        context["title"] = "Ajouter actes de mariage"
        context["form_title"] = "ACTE DE MARIAGE"
        template = loader.get_template("Actes/templates2.html")
        return HttpResponse(template.render(context = context,request = request))

