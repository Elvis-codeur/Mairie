
LINKS = {}

LINKS["dashboard"] = ("officier/dashboard/<str:message>",r"officier/dashboard/")
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
LINKS["maire-add-off"] = ("maire/add/officier/<str:message>",)

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

# Pour imprimer les transcription
LINKS["print-naissance-trans"] = ("officier/imprimer/naissance/transcription/<str:message>",)
LINKS["print-deces-trans"] = ("officier/imprimer/deces/transcription/<str:message>",)
LINKS["print-mariage-trans"] = ("officier/imprimer/mariage/transcription/<str:message>",)