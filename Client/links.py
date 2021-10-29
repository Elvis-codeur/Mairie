
LINKS = {}

LINKS["dashboard"] = ("dashboard/<str:message>",r"dashboard/")
LINKS["add-naissance"] = ("add/naissance/<str:message>",r"add/naissance/")
LINKS["add-deces"] = ("add/deces/<str:message>",r"add/deces/")
LINKS["add-mariage"] = ("add/mariage/<str:message>",r"add/mariage/")
LINKS["officier-view"] = ("officier/compte_vue/<str:message>","officier/compte_vue/")

# Pour le maire
LINKS["maire dahboard"] = ("maire/dashboard/<str:message>","maire/dashboard/")
LINKS["maire-naissance"] = ("maire/naissance/<str:message>",r"add/naissance/")
LINKS["maire-deces"] = ("maire/deces/<str:message>",r"add/deces/")
LINKS["maire-mariage"] = ("maire/mariage/<str:message>",r"add/mariage/")
LINKS["maire-compte"] = ("maire/compte_vue/<str:message>","maire/compte_vue/")
LINKS["maire-add-off"] = ("maire/add/officier/<str:message>",)
# Pour les autres
LINKS["modify-naissance"] = ("modifier/naissance/<str:message>","modifier/naissance/")