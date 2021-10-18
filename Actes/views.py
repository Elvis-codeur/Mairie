from django import template
from django.forms.forms import Form
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from Actes.forms import *
from Actes.verifications import *

def p(request):
    if(request.method == "POST"):
        form = ActesNaissanceForm(request.POST,request.FILES)
        #print(request.POST)
        if(form.is_valid()):
            #print(form.cleaned_data)
            #print(save_acte_naissance(form.cleaned_data))
            return HttpResponse(generate_actes_naissance(form.cleaned_data))

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
        template = loader.get_template("Actes/templates2.html")
        return HttpResponse(template.render(context = context,request = request))

def receive_naissance(request):
    if(request.method == "GET"):
        print("\n\n",request.read())

    
def index(request):
    context = {}    
    template = loader.get_template("Actes/index.html")
    return HttpResponse(template.render(context = context,request = request))
    
# Create your views here.
