
LINKS = {}

LINKS["dashboard"] = ("officier/dashboard/<str:message>",r"officier/dashboard/")

LINKS["dashboard-naissance"] =("officier/dashboard/naissance/<str:message>",r"officier/dashboard/")
LINKS["dashboard-deces"] =("officier/dashboard/deces/<str:message>",r"officier/dashboard/")
LINKS["dashboard-mariage"] =("officier/dashboard/mariage/<str:message>",r"officier/dashboard/")


LINKS["add-naissance"] = ("officier/add/naissance/<str:message>",r"officier/add/naissance/")
LINKS["add-deces"] = ("officier/add/deces/<str:message>",r"officier/add/deces/")
LINKS["add-mariage"] = ("officier/add/mariage/<str:message>",r"officier/add/mariage/")
LINKS["officier-view"] = ("officier/compte_vue/<str:message>","officier/compte_vue/")

# Pour le maire
LINKS["maire dahboard"] = ("maire/dashboard/<str:message>","maire/dashboard/")
LINKS["maire-naissance"] = ("maire/naissance/<str:message>",r"add/naissance/")
LINKS["maire-deces"] = ("maire/deces/<str:message>",r"add/deces/")
LINKS["maire-mariage"] = ("maire/mariage/<str:message>",r"add/mariage/")
LINKS["maire-compte"] = ("maire/compte_vue/<str:message>","maire/compte_vue/")
LINKS["maire-officer-account"]=("maire/officier/compte_vue/<str:message>","maire/compte_vue/")
LINKS["maire-add-off"] = ("maire/add/officier/<str:message>",)
# Pour voir maire
LINKS["maire-view-naissance"] = ("maire/voir/naissance/<str:message>",)
LINKS["maire-view-deces"] = ("maire/voir/deces/<str:message>",)
LINKS["maire-view-mariage"] = ("maire/voir/mariage/<str:message>",)
# Pour les modifications
LINKS["maire-modify-naissance"] = ("maire/modifier/naissance/<str:message>","modifier/naissance/")
LINKS["maire-modify-deces"] = ("maire/modifier/deces/<str:message>","officier/modifier/deces/")
LINKS["maire-modify-mariage"] = ("maire/modifier/mariage/<str:message>","officer/modifier/mariage/")
# Pour voir les transcription
LINKS["maire-view-naissance-trans"] = ("maire/voir/naissance/transcription/<str:message>",)
LINKS["maire-view-deces-trans"] = ("maire/voir/deces/transcription/<str:message>",)
LINKS["maire-view-mariage-trans"] = ("maire/voir/mariage/transcription/<str:message>",)



# Pour les modifications
LINKS["modify-naissance"] = ("officier/modifier/naissance/<str:message>","modifier/naissance/")
LINKS["modify-deces"] = ("officier/modifier/deces/<str:message>","officier/modifier/deces/")
LINKS["modify-mariage"] = ("officer/modifier/mariage/<str:message>","officer/modifier/mariage/")


# Pour voir
LINKS["view-naissance"] = ("officier/voir/naissance/<str:message>",)
LINKS["view-deces"] = ("officier/voir/deces/<str:message>",)
LINKS["view-mariage"] = ("officier/voir/mariage/<str:message>",)

# Pour voir les transcription
LINKS["view-naissance-trans"] = ("officier/voir/naissance/transcription/<str:message>",)
LINKS["view-deces-trans"] = ("officier/voir/deces/transcription/<str:message>",)
LINKS["view-mariage-trans"] = ("officier/voir/mariage/transcription/<str:message>",)

# Pour imprimer
LINKS["print-naissance"] = ("officier/imprimer/naissance/<str:message>",)
LINKS["print-deces"] = ("officier/imprimer/deces/<str:message>",)
LINKS["print-mariage"] = ("officier/imprimer/mariage/<str:message>",)

# Pour faire les pdf 
LINKS["print-pdf-naissance"] = ("officier/imprimer/naissance/pdf/<str:message>/<int:number>",)
LINKS["print-pdf-deces"] = ("officier/imprimer/deces/pdf/<str:message>/<int:number>",)
LINKS["print-pdf-mariage"] = ("officier/imprimer/mariage/pdf/<str:message>/<int:number>",)

# Pour imprimer les transcriptions
LINKS["print-naissance-trans"] = ("officier/imprimer/naissance/transcription/<str:message>",)
LINKS["print-deces-trans"] = ("officier/imprimer/deces/transcription/<str:message>",)
LINKS["print-mariage-trans"] = ("officier/imprimer/mariage/transcription/<str:message>",)

# Pour imprimer les pdf des transcriptions
LINKS["print-pdf-naissance-trans"] = ("officier/imprimer/naissance/transcription/pdf/<str:message>/<int:number>",)
LINKS["print-pdf-deces-trans"] = ("officier/imprimer/deces/transcription/pdf/<str:message>/<int:number>",)
LINKS["print-pdf-mariage-trans"] = ("officier/imprimer/mariage/transcription/pdf/<str:message>/<int:number>",)



# Pour la connexion
LINKS["conn-maire"] = ("connexion/maire",)
LINKS["conn-officier"] = ("connexion/officier",)

# Pour la deconnection
LINKS["deconn-maire"] = ("deconnexion/maire",)
LINKS["deconn-officier"] = ("deconnexion/officier",)