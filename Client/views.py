from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.http.response import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from django.template import loader
from Actes.forms import *
from Actes.verifications import *
from Client.algorithms import *
from Client.forms import *
from Client.models import *
# Create your views here.

officier_login_url ="/fr/clients/connexion/officier"
maire_login_url = "/fr/clients/connexion/maire"

@login_required(login_url=officier_login_url)
def dashboard(request,message):

    if(request.method == "POST"):
        a = 0

    else:
        context = {}
        f = SearchForm()
        f1 = ActesChoiceForm()
        context["form"] =f
        context["form1"] = f1
        context["links"] = create_links(langue="fr",request=request)
        context["message"] = message
        context["list"] = prepare_html_list("mariage",message)

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_officier")

        template = loader.get_template("Actes/officiers_vue.html")
        return HttpResponse(template.render(context = context,request = request))
    
    

    
    
@login_required(login_url=officier_login_url)
def add_naissance(request,message):
    if(request.method == "POST"):
        form = ActesNaissanceForm(request.POST,request.FILES)
        #print(request.POST)
        if(form.is_valid()):
            #print(form.cleaned_data)
            i = save_acte_naissance(form.cleaned_data)
            a = parse_message(message)
            a["ident"] = i
            save_journal(a,"naissance")
            


            #return HttpResponse(generate_actes_naissance(form.cleaned_data))
            return redirect(reverse("Client:dashboard",kwargs={"message":message}))
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
        context["message"] = message

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_officier")

        template = loader.get_template("Actes/templates2.html")
        return HttpResponse(template.render(context = context,request = request))


@login_required(login_url=officier_login_url)
def modify_naissance(request,message):
    if(request.method == "POST"):
        form = ActesNaissanceForm(request.POST,request.FILES)
        #print(request.POST)
        if(form.is_valid()):
            #print(form.cleaned_data)
            i = save_acte_naissance(form.cleaned_data,modify=True,message=message)
            a = parse_message(message)
            a["ident"] = i
            save_journal(a,"naissance")
            


            #return HttpResponse(generate_actes_naissance(form.cleaned_data))
            return redirect(reverse("Client:dashboard",kwargs={"message":message}))
        else:
            print("LOSE")
        return HttpResponse("none")
    else:
        form = ActesNaissanceForm(auto_id=True)
        me = parse_message(message)

        model = get_actesnaissance_by_id(me["naissance"])
        kl = model.__dict__

        l =[]
        compteur = 0
        for i in form:
            compteur += 1
            dic = {}
            dic["f"]= i
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
        context["message"] = message

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_officier")
    
        template = loader.get_template("Actes/templates2.html")
        return HttpResponse(template.render(context = context,request = request))


@login_required(login_url=officier_login_url)
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
            save_journal(a,"deces")
            
            return redirect(reverse("Client:dashboard",kwargs={"message":message}))
            
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
        context["message"] = message

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_officier")
    
        template = loader.get_template("Actes/templates2.html")
        return HttpResponse(template.render(context = context,request = request))



@login_required(login_url=officier_login_url)
def modify_deces(request,message):
    if(request.method == "POST"):
        form = ActesNaissanceForm(request.POST,request.FILES)
        #print(request.POST)
        if(form.is_valid()):
            #print(form.cleaned_data)
            i = save_acte_naissance(form.cleaned_data)
            a = parse_message(message)
            a["ident"] = i
            save_journal(a,"naissance")
            


            #return HttpResponse(generate_actes_naissance(form.cleaned_data))
            return redirect(reverse("Client:dashboard",kwargs={"message":message}))
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
        context["message"] = message

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_officier")
    
        template = loader.get_template("Actes/templates2.html")
        return HttpResponse(template.render(context = context,request = request))


@login_required(login_url=officier_login_url)
def add_mariage(request,message):
    if(request.method == "POST"):
        form = ActesMariageForm(request.POST,request.FILES)
        #print(request.POST)
        if(form.is_valid()):
            #print(form.cleaned_data)
            i = save_actes_mairiage(form.cleaned_data)
            a = parse_message(message)
            a["ident"] = i
            save_journal(a,"mariage")

            #pdf = generate_actes_deces(form.cleaned_data)

            #response = HttpResponse(bytes(pdf),content_type='application/pdf')
            #response['Content-Disposition'] = 'filename=some_file.pdf'
            return redirect(reverse("Client:dashboard",kwargs={"message":message}))
            

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
        context["message"] = message

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_officier")
    
        template = loader.get_template("Actes/templates2.html")
        return HttpResponse(template.render(context = context,request = request))


@login_required(login_url=officier_login_url)
def modify_mariage(request,message):
    if(request.method == "POST"):
        form = ActesNaissanceForm(request.POST,request.FILES)
        #print(request.POST)
        if(form.is_valid()):
            #print(form.cleaned_data)
            i = save_acte_naissance(form.cleaned_data)
            a = parse_message(message)
            a["ident"] = i
            save_journal(a,"naissance")
            


            #return HttpResponse(generate_actes_naissance(form.cleaned_data))
            return redirect(reverse("Client:dashboard",kwargs={"message":message}))
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
        context["message"] = message

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_officier")
    
        template = loader.get_template("Actes/templates2.html")
        return HttpResponse(template.render(context = context,request = request))


@login_required(login_url=officier_login_url)
def account_view(request,message):
    if(request.method == "POST"):
        a  = 0

    else:
        a = parse_message(message)
        executant = get_executant_by_id(a["executant"])

        element = generate_compte_view(executant)
        print(element)
        l = []
        for i in list(element.keys()):
            b = {}
            b["label"] = i +":"
            b["f"] = element[i]
            b["containner"] = "col-12s"
            l.append(b)

        context = {}
        context["message"] = message
        context["form"] = l
        template = loader.get_template("Actes/compte_vue.html")

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_officier")
    
        return HttpResponse(template.render(context = context,request = request))


@login_required(login_url=maire_login_url)
def maire_dashboard(request,message):
    
    if(request.method == "POST"):
        a = 0
    else:


        context = {}
        context["message"] = message
        context["table_title"] = "Vos  officiers "
        context["list"] = prepare_maire_html_list("executant",0,message)
        context["col_head"] = create_col_head(["Nom","Prenom","email","Numéro"])
        context["dashboard"] = "True"


        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_maire")
    
        template = loader.get_template("Actes/maire_vue.html")
        return HttpResponse(template.render(context = context,request = request))


@login_required(login_url=maire_login_url)
def maire_naissance_view(request,message):
    if(request.method == "POST"):
        a = 0
    else:

        
        context = {}
        context["message"] = message
        context["list"] = prepare_maire_html_list("naissance",0,message)
        context["col_head"] = create_col_head(["Nom","Prenom","Officiers"])

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_maire")
    
        template = loader.get_template("Actes/maire_vue.html")
        return HttpResponse(template.render(context = context,request = request))


@login_required(login_url=maire_login_url)
def maire_deces_view(request,message):
    if(request.method == "POST"):
        a = 0
    else:

        
        context = {}
        context["message"] = message
        context["list"] = prepare_maire_html_list("deces",0,message)
        context["col_head"] = create_col_head(["Nom","Prenom","Officiers"])

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_maire")
    
        template = loader.get_template("Actes/maire_vue.html")
        return HttpResponse(template.render(context = context,request = request))


@login_required(login_url=maire_login_url)
def maire_mariage_view(request,message):
    if(request.method == "POST"):
        a = 0
    else:

        
        context = {}
        context["message"] = message
        context["list"] = prepare_maire_html_list("mariage",0,message)
        context["col_head"] = create_col_head(["Nom","Prenom","Officiers"])

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_maire")
    
        template = loader.get_template("Actes/maire_vue.html")
        return HttpResponse(template.render(context = context,request = request))


@login_required(login_url=maire_login_url)
def maire_account_view(request,message):
    if(request.method == "POST"):
        a  = 0

    else:
        a = parse_message(message)
        maire = get_maire_by_id(a["maire"])
        element = generate_compte_view(maire)
        print(element)
        l = []
        for i in list(element.keys()):
            b = {}
            b["label"] = i +":"
            b["f"] = element[i]
            b["containner"] = "col-12s"
            l.append(b)

        context = {}
        context["message"] = message
        context["form"] = l

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_maire")
    

        template = loader.get_template("Actes/maire_compte_vue.html")

        return HttpResponse(template.render(context = context,request = request))

@login_required(login_url=maire_login_url)
def maire_officier_account_view(request,message):
    if(request.method == "POST"):
        a  = 0

    else:

        a = parse_message(message)
        executant = get_executant_by_id(a["executant"])

        element = generate_compte_view(executant)
        print(element)
        l = []
        for i in list(element.keys()):
            b = {}
            b["label"] = i +":"
            b["f"] = element[i]
            b["containner"] = "col-12s"
            l.append(b)

        context = {}
        context["message"] = message
        context["form"] = l
        context["maire"]="a"
        template = loader.get_template("Actes/compte_vue.html")
        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_maire")

        return HttpResponse(template.render(context = context,request = request))



@login_required(login_url=maire_login_url)
def maire_add_officier(request,message):
    if(request.method == "POST"):
        form = ExecutantForm(request.POST,request.FILES)
        #print(request.POST)
        if(form.is_valid()):

            save_executant(form.cleaned_data,parse_message(message))
            return redirect(reverse("Client:maire_account_view",kwargs={"message":message}))
        else:
            print(form.cleaned_data)
            return redirect(reverse("Client:dashboard",kwargs={"message":message}))
    else:
        form = ExecutantForm(auto_id=True)
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
        context["title"] = "Ajouter un officiers"
        context["form_title"] = "OFFICIERS"
        context["message"] = message
        context["dashboard"] = "True"

        #Pour la déconnection
        context["disconnect"] = reverse("Client:deconnexion_maire")
    
        template = loader.get_template("Actes/maire_add_template.html")
        return HttpResponse(template.render(context = context,request = request))
    

@login_required(login_url=officier_login_url)
def officier_naissance_vue(request,message):


    template = loader.get_template("Actes/acte_vue.html")
    l = generate_acte_naissance_fromdb(message)
    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Ajouter un officiers"
    context["form_title"] = "NAISSANCE"
    context["acte_modification"] = "True"
    context["acte"] = "naissance"
    context["acte_mod_link"] = reverse("Client:modify_naissance",kwargs={"message":message})
    
    
    #Pour les fichiers
    context["no_print"] ="True"
    me = parse_message(message)
    m = get_actesnaissance_by_id(me["naissance"])
    context["original_url"] = m.original.url
    context["tran_url"] = m.transcription.url
    #Pour l'impression
    context["print_link"] = reverse("Client:print_naissance",kwargs={"message":message})

    # POur la transciption
    context["trans_ori"] = "la transcription"
    context["acte_trans_link"] = reverse("Client:officier_naissance_transcription_vue",kwargs={"message":message} )

    
    # Pour l'entête
    me = parse_message(message)
    a = get_actesnaissance_by_id(me["naissance"]).__dict__

    # Pour le bas 
    context["naissance_footer"] = "True"

    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1

    context["re"] = kl
    context["message"] = message

    

    return HttpResponse(template.render(context))


@login_required(login_url=officier_login_url)
def officier_naissance_transcription_vue(request,message):


    template = loader.get_template("Actes/acte_vue.html")
    l = generate_acte_naissance_fromdb(message)
    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Ajouter un officiers"
    context["form_title"] = "NAISSANCE"
    context["acte_modification"] = "True"
    context["acte"] = "naissance"
    context["acte_mod_link"] = reverse("Client:modify_naissance",kwargs={"message":message})
    
    #Pour les fichiers
    context["no_print"] ="True"
    me = parse_message(message)
    m = get_actesnaissance_by_id(me["naissance"])
    context["original_url"] = m.original.url
    context["tran_url"] = m.transcription.url


    #Pour l'impression
    context["print_link"] = reverse("Client:print_transcription_naissance",kwargs={"message":message}) 

    # POur la transciption
    context["trans_ori"] = "l'original"
    context["acte_trans_link"] = reverse("Client:officier_naissance_vue",kwargs={"message":message} )
    context["tran_footer"] = "True"

    # Pour l'entête
    me = parse_message(message)
    a = get_actesnaissance_by_id(me["naissance"]).__dict__

    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1

    

    context["re"] = kl
    context["message"] = message
    return HttpResponse(template.render(context))



@login_required(login_url=officier_login_url)
def officier_deces_vue(request,message):
    """Cette méthode permet à l'officier de voir un acte de deces"""

    template = loader.get_template("Actes/acte_vue.html")
    l = generate_acte_deces_fromdb(message)
    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Ajouter un officiers"
    context["form_title"] = "DECES"
    context["acte_modification"] = "True"
    context["acte"] = "deces"
    context["acte_mod_link"] = reverse("Client:modify_deces",kwargs={"message":message})
    
    #Pour les fichiers
    context["no_print"] ="True"
    me = parse_message(message)
    m = get_actesdeces_by_id(me["deces"])
    context["original_url"] = m.original.url
    context["tran_url"] = m.transcription.url

    #Pour l'impression
    context["print_link"] = reverse("Client:print_deces",kwargs={"message":message}) 

    context["message"] = message

    # POur la transciption
    context["trans_ori"] = "la transcription"
    context["acte_trans_link"] = reverse("Client:officier_deces_transcription_vue",kwargs={"message":message} )


    # Pour l'entête
    me = parse_message(message)
    a = get_actesdeces_by_id(me["deces"]).__dict__

    # Pour le bas
    context["deces_footer"] = "True"

    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1

    context["re"] = kl
    return HttpResponse(template.render(context))
    

@login_required(login_url=officier_login_url)
def officier_deces_transcription_vue(request,message):
    """Cette méthode permet à l'officier de voir un acte de deces"""

    template = loader.get_template("Actes/acte_vue.html")
    l = generate_acte_deces_fromdb(message)
    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Ajouter un officiers"
    context["form_title"] = "DECES"
    context["acte_modification"] = "True"
    context["acte"] = "deces"
    context["acte_mod_link"] = reverse("Client:modify_deces",kwargs={"message":message})
    
    #Pour les fichiers
    context["no_print"] ="True"
    me = parse_message(message)
    m = get_actesdeces_by_id(me["deces"])
    context["original_url"] = m.original.url
    context["tran_url"] = m.transcription.url

    #Pour l'impression
    context["print_link"] = reverse("Client:print_transcription_deces",kwargs={"message":message})

    context["message"] = message

    # POur la transciption
    context["trans_ori"] = "l'original"
    context["acte_trans_link"] = reverse("Client:officier_deces_vue",kwargs={"message":message} )
    context["tran_footer"] = "True"

    # Pour l'entête
    me = parse_message(message)
    a = get_actesdeces_by_id(me["deces"]).__dict__

    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1

    context["re"] = kl
    return HttpResponse(template.render(context))


@login_required(login_url=officier_login_url)
def officier_mariage_vue(request,message):
    """Cette méthode permet à l'officier de voir les actes de mariage"""

    # Pour l'entête
    me = parse_message(message)
    a = get_actesmariage_by_id(me["mariage"]).__dict__

    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1


    template = loader.get_template("Actes/acte_vue.html")
    l = generate_acte_mariage_fromdb(message)
    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Voir un acte de mariage"
    context["form_title"] = "MARIAGE"
    #Pour la modification
    context["acte_modification"] = "True"
    context["acte"] = "mariage"

    
    context["acte_mod_link"] = reverse("Client:modify_mariage",kwargs={"message":message})
    
    # POur la transciption
    context["trans_ori"] = "la transcription"
    context["acte_trans_link"] = reverse("Client:officier_mariage_transcription_vue",kwargs={"message":message} )

    #Pour les fichiers
    context["no_print"] ="True"
    me = parse_message(message)
    m = get_actesmariage_by_id(me["mariage"])
    context["original_url"] = m.original.url
    context["tran_url"] = m.transcription.url
    #Pour l'impression
    
    context["print_link"] = reverse("Client:print_mariage",kwargs={"message":message})

    context["message"] = message

    #Pour l'entete
    context["re"] = kl

    #Pour le bas
    context["mariage_footer"] = "True"
    
    return HttpResponse(template.render(context,request=request))

@login_required(login_url=officier_login_url)  
# Transcription mariage
def officier_mariage_transcription_vue(request,message):
    """Cette méthode permet à l'officier de voir les actes de mariage"""

    # Pour l'entête
    me = parse_message(message)
    a = get_actesmariage_by_id(me["mariage"]).__dict__

    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1


    template = loader.get_template("Actes/acte_vue.html")
    l = generate_acte_mariage_fromdb(message)
    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Voir un acte de mariage"
    context["form_title"] = "MARIAGE"
    #Pour la modification
    context["acte_modification"] = "True"
    context["acte"] = "mariage"
    context["acte_mod_link"] = reverse("Client:modify_mariage",kwargs={"message":message})
    
    #Pour les fichiers
    context["no_print"] ="True"
    me = parse_message(message)
    m = get_actesmariage_by_id(me["mariage"])
    context["original_url"] = m.original.url
    context["tran_url"] = m.transcription.url

    #Pour l'impression
    context["print_link"] = reverse("Client:print_transcription_mariage",kwargs={"message":message}) 

    # POur la transciption
    context["trans_ori"] = "l'original"
    context["acte_trans_link"] = reverse("Client:officier_mariage_vue",kwargs={"message":message} )
    context["tran_footer"] = "True"

    context["message"] = message

    #Pour l'entete
    context["re"] = kl
    
    return HttpResponse(template.render(context))
    


@login_required(login_url=officier_login_url)
# Pour imprimer #######################
def print_naissance(request,message):
    """Cette méthode permet à l'officier d'imprimer les actes de mariage"""

    l = generate_acte_naissance_fromdb(message)


    # Pour l'entête
    me = parse_message(message)
    a = get_actesnaissance_by_id(me["naissance"]).__dict__


    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1


    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Imprimer un acte de naissance"
    context["form_title"] = "ACTE DE NAISSANCE   N°"
    context["message"] = message
    context["re"] = kl

    # Pour le bas
    context["naissance_footer"] = "True"

    template = loader.get_template("Actes/acte_print.html")

    # Pour l'impression on écrit dans un fichier temporaire
    name = random.randint(0,10**6)
    f = open("Actes/templates/Actes/{}.html".format(name),"w")
    f.write(str(template.render(context)))
    f.close()

    l = str(reverse("Client:print_naissance_pdf",
                kwargs={"message":message,"number":name}))

    a = pdfkit.from_url(l,False)

    response = HttpResponse(str(a),content_type='application/pdf')
    response['Content-Disposition'] = 'filename=some_file.pdf'
    
    return response


@login_required(login_url=officier_login_url)
def print_naissance_transcription(request,message):
    """Cette méthode permet à l'officier d'imprimer les actes de mariage"""

    l = generate_acte_naissance_fromdb(message)


    # Pour l'entête
    me = parse_message(message)
    a = get_actesnaissance_by_id(me["naissance"]).__dict__

    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1


    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Imprimer un acte de naissance"
    context["form_title"] = "ACTE DE NAISSANCE   N°"
    context["message"] = message
    context["re"] = kl

    # Pour le bas et la transcription
    context["tran_footer"] = "True"

    template = loader.get_template("Actes/acte_print.html")
    
    # Pour l'impression on écrit dans un fichier temporaire
    name = random.randint(0,10**6)
    f = open("Actes/templates/Actes/{}.html".format(name),"w")
    f.write(str(template.render(context)))
    f.close()

    l = str(reverse("Client:print_transcription_naissance_pdf",
                kwargs={"message":message,"number":name}))

    a = pdfkit.from_url(l,False)

    response = HttpResponse(str(a),content_type='application/pdf')
    response['Content-Disposition'] = 'filename=some_file.pdf'
    
    return response




@login_required(login_url=officier_login_url)
def print_deces(request,message):
    """Cette méthode permet à l'officier d'imprimer les actes deces"""

    l = generate_acte_deces_fromdb(message)

    # Pour l'entête
    me = parse_message(message)
    a = get_actesdeces_by_id(me["deces"]).__dict__

    


    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1


    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Imprimer un acte de naissance"
    context["form_title"] = "ACTE DE DECES   N°"
    context["message"] = message
    context["re"] = kl

    # Pour le bas
    context["deces_footer"] = "Treu"

    template = loader.get_template("Actes/acte_print.html")

    
    # Pour l'impression on écrit dans un fichier temporaire
    name = random.randint(0,10**6)
    f = open("Actes/templates/Actes/{}.html".format(name),"w")
    f.write(str(template.render(context)))
    f.close()

    l = str(reverse("Client:print_deces_pdf",
                kwargs={"message":message,"number":name}))

    a = pdfkit.from_url(l,False)

    response = HttpResponse(str(a),content_type='application/pdf')
    response['Content-Disposition'] = 'filename=some_file.pdf'
    
    return response


@login_required(login_url=officier_login_url)
def print_deces_transcription(request,message):
    """Cette méthode permet à l'officier d'imprimer les actes deces"""

    l = generate_acte_deces_fromdb(message)

    # Pour l'entête
    me = parse_message(message)
    a = get_actesdeces_by_id(me["deces"]).__dict__

    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1


    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Imprimer un acte de naissance"
    context["form_title"] = "ACTE DE DECES   N°"
    context["message"] = message
    context["re"] = kl

    # Pour le bas
    context["tran_footer"] = "True"
    template = loader.get_template("Actes/acte_print.html")
    
    # Pour l'impression on écrit dans un fichier temporaire
    name = random.randint(0,10**6)
    f = open("Actes/templates/Actes/{}.html".format(name),"w")
    f.write(str(template.render(context)))
    f.close()

    l = str(reverse("Client:print_transcription_deces_pdf",
                kwargs={"message":message,"number":name}))

    a = pdfkit.from_url(l,False)

    response = HttpResponse(str(a),content_type='application/pdf')
    response['Content-Disposition'] = 'filename=some_file.pdf'
    
    return response



@login_required(login_url=officier_login_url)
def print_mariage(request,message):
    """Cette méthode permet à l'officier d'imprimer les actes de mariage"""

    l = generate_acte_mariage_fromdb(message)
    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Voir un acte de mariage"
    context["form_title"] = "ACTE DE MARIAGE   N°"
    
    # Pour l'entête
    me = parse_message(message)
    a = get_actesmariage_by_id(me["mariage"]).__dict__

    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1


    context["message"] = message
    context["re"] = kl

    # Pour les footers

    context["mariage_footer"] = "True"
    #context["tran_footer"] = "True"

    template = loader.get_template("Actes/acte_print.html")
    
    # Pour l'impression on écrit dans un fichier temporaire
    name = random.randint(0,10**6)
    f = open("Actes/templates/Actes/{}.html".format(name),"w")
    f.write(str(template.render(context)))
    f.close()

    l = str(reverse("Client:print_mariage_pdf",
                kwargs={"message":message,"number":name}))

    a = pdfkit.from_url(l,False)

    response = HttpResponse(str(a),content_type='application/pdf')
    response['Content-Disposition'] = 'filename=some_file.pdf'
    
    return response


@login_required(login_url=officier_login_url)
def print_mariage_transcription(request,message):
    """Cette méthode permet à l'officier d'imprimer les actes de mariage"""

    l = generate_acte_mariage_fromdb(message)
    context = {}
    context["form"] = l#l[:len(l)-1]
    context["title"] = "Imprimer une actes de mariage"
    context["form_title"] = "ACTE DE MARIAGE  N°"
    
    # Pour l'entête
    me = parse_message(message)
    a = get_actesmariage_by_id(me["mariage"]).__dict__

    kl = {}
    compteur = 0
    for i in list(a.keys())[2:7]:
        kl[i] = a[i]
        compteur = compteur+1


    context["message"] = message
    context["re"] = kl

    # Pour les footers

    #context["naissance_footer"] = "True"
    context["tran_footer"] = "True"

    template = loader.get_template("Actes/acte_print.html")

    # Pour l'impression on écrit dans un fichier temporaire
    name = random.randint(0,10**6)
    f = open("Actes/templates/Actes/{}.html".format(name),"w")
    f.write(str(template.render(context)))
    f.close()

    l = str(reverse("Client:print_transcription_mariage_pdf",
                kwargs={"message":message,"number":name}))

    a = pdfkit.from_url(l,False)

    response = HttpResponse(str(a),content_type='application/pdf')
    response['Content-Disposition'] = 'filename=some_file.pdf'
    
    return response




def maire_login(request):
    if request.method == "POST":
        form = MaireLoginForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)
                message = create_url_message(create_message(user),action="login")

                a = reverse("Client:maire_account_view",kwargs ={"message":message})
                return HttpResponseRedirect(a)
            else:
                return HttpResponse("HHHJHHHS")

        else:
            print(form.cleaned_data)
            return HttpResponse("jhhjh")

    else:
        if request.user.is_authenticated: 
            message = create_url_message(create_message(request.user),action="login")
            a = reverse("Client:maire_account_view",kwargs ={"message":message})
            return HttpResponseRedirect(a)
        
        else:
            print("ELvisjksd")
            form = MaireLoginForm()
            context = {}
            context["form"] = form
            template = loader.get_template("Actes/login_template.html")
            return HttpResponse(template.render(request = request,context = context))
        


def officier_login(request):
    if request.method == "POST":
        form = OfficierLoginForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)

                message = create_url_message(create_message(user),action="login")

                a = reverse("Client:dashboard",kwargs ={"message":message})
                return HttpResponseRedirect(a)
            else:
                return HttpResponse("HHHJHHHS")

        else:
            print(form.cleaned_data)
            return HttpResponse("jhhjh")

    else:
        if request.user.is_authenticated:
            #print("lEIVSISDIIO")
            message = create_url_message(create_message(request.user),action="login")
            a = reverse("Client:dashboard",kwargs ={"message":message})
            return HttpResponseRedirect(a)
        
        else:
            #print("ELvisjksd")
            form = OfficierLoginForm()
            context = {}
            context["form"] = form
            template = loader.get_template("Actes/login_template.html")
            return HttpResponse(template.render(request = request,context = context))
        
       

@login_required(login_url=officier_login_url)
def officier_deconnect(request):
    logout(request)
    a = reverse("Client:connexion_officier")
    return HttpResponseRedirect(a)


def maire_deconnect(request):
    logout(request)
    a = reverse("Client:connexion_maire")
    return HttpResponseRedirect(a)


def print_naissance_pdf(request,message,number):

    context = {}
    template = loader.get_template("Actes/{}.html".format(number))
    return HttpResponse(template.render(context,request=request))

def print_deces_pdf(request,message,number):

    context = {}
    template = loader.get_template("Actes/{}.html".format(number))
    return HttpResponse(template.render(context,request=request))

def print_mariage_pdf(request,message,number):

    context = {}
    template = loader.get_template("Actes/{}.html".format(number))
    return HttpResponse(template.render(context,request=request))


def print_naissance_transcription_pdf(request,message,number):

    context = {}
    template = loader.get_template("Actes/{}.html".format(number))
    return HttpResponse(template.render(context,request=request))

def print_deces_transcription_pdf(request,message,number):

    context = {}
    template = loader.get_template("Actes/{}.html".format(number))
    return HttpResponse(template.render(context,request=request))

def print_mariage_transcription_pdf(request,message,number):

    context = {}
    template = loader.get_template("Actes/{}.html".format(number))
    return HttpResponse(template.render(context,request=request))

def get_element(request,code):

    if(code == "1"):
        a = ActesNaissanceModel.objects.all()
        l =""
        for i in a:
            l = i.le + "," +i.nom+","+i.prenom + ";"

        return HttpResponse(l)

    elif(code == "2"):
        a = ActesMariageModel.objects.all()
        l =""
        for i in a:
            l = i.le + "," +i.nom+","+i.prenom + ";"
            
        return HttpResponse(l)
    else:
        return ActesDecesModel.objects.all()
