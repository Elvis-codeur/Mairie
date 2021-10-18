from django.contrib import admin

from Actes.models import *

class ActesNaissanceModelAdmin(admin.ModelAdmin):
    list_display = ("le","nom","prenom")


admin.site.register(ActesNaissanceModel,ActesNaissanceModelAdmin)


# Register your models here.
