from django.contrib import admin
from .models import Ruche, Rucher, Reine

# Register your models here.

@admin.register(Ruche)
class RucheAdmin(admin.ModelAdmin):
    list_display = ('nom','id_reine', 'date_inspection', 'niveaux_miel', 'infestations')


@admin.register(Rucher)
class RucherAdmin(admin.ModelAdmin):
    list_display = ('nom', 'emplacement', 'date_creation')
  

@admin.register(Reine)
class ReineAdmin(admin.ModelAdmin):
    list_display = ('id_reine', 'age', 'sante', 'date_remplacement')
  