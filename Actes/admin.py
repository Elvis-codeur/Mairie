from django.contrib import admin

from Actes.models import *

class ActesNaissanceModelAdmin(admin.ModelAdmin):
    list_display = ("le","nom","prenom")
    ordering = ("nom",)
    search_fields = ("prenom",)

class ActesMariageModelAdmin(admin.ModelAdmin):
    list_display = ("le","nom1","nom2")
    ordering = ("nom1","nom2")
    search_fields = ("nom1","nom2")

class ActesDecesModelAdmin(admin.ModelAdmin):
    list_display = ("le","nom","prenom")
    ordering = ("nom",)
    search_fields = ("prenom","nom")

admin.site.register(ActesNaissanceModel,ActesNaissanceModelAdmin)
admin.site.register(ActesDecesModel,ActesDecesModelAdmin)
admin.site.register(ActesMariageModel,ActesMariageModelAdmin)


# Register your models here.
