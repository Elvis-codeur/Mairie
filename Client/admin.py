from django.contrib import admin
from .models import *

class MaireAdmin(admin.ModelAdmin):
    list_display = ("nom","prenom")

class MairieAdmin(admin.ModelAdmin):
    list_display = ("nom","addresse")

class ExecutantAdmin(admin.ModelAdmin):
    list_display = ("nom","prenom")

class NaissanceJournalAdmin(admin.ModelAdmin):
    list_display = ("date_first_creation","mairie","maire","executant","naissance")

class DecesJournalAdmin(admin.ModelAdmin):
    list_display = ("date_first_creation","mairie","maire","executant","deces")

class MariageJournalAdmin(admin.ModelAdmin):
    list_display = ("date_first_creation","mairie","maire","executant","mariage")




admin.site.register(Maire,MaireAdmin)
admin.site.register(Mairie,MairieAdmin)
admin.site.register(Executant,ExecutantAdmin)
admin.site.register(NaissanceJournal,NaissanceJournalAdmin)
admin.site.register(DecesJournal,DecesJournalAdmin)
admin.site.register(MariageJournal,MariageJournalAdmin)
# Register your models here.
