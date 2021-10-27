
LINKS = {}

LINKS["dashboard"] = ("dashboard/<str:message>",r"dashboard/")
LINKS["add-naissance"] = ("add/naissance/<str:message>",r"add/naissance/")
LINKS["add-deces"] = ("add/deces/<str:message>",r"add/deces/")
LINKS["add-mariage"] = ("add/mariage/<str:message>",r"add/mariage/")
LINKS["officier-view"] = ("officier/compte_vue/<str:message>","officier/compte_vue/")
LINKS["maire dahboard"] = ("maire/dashboard/<str:message>","maire/dashboard/")