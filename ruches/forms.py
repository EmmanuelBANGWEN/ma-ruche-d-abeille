from django import forms
from .models import Ruche, Reine, Recolte, Rucher
from django.contrib import admin


# @admin.register(Ruche)
class RucheForm(forms.ModelForm):
    class Meta:
        model = Ruche
        fields = ['rucher', 'id_reine', 'nom', 'date_inspection', 'niveaux_miel', 'infestations']

# @admin.register(Reine)
# class ReineForm(forms.ModelForm):
#     class Meta:
#         model = Reine
#         fields = ['id_reine', 'rucher', 'age', 'sante', 'date_remplacement']

# @admin.register(Recolte)


class RecolteForm(forms.ModelForm):
    class Meta:
        model = Recolte
        fields = ['ruche', 'date_recolte', 'quantite_miel']

        widgets = {
            'date_recolte': forms.DateInput(attrs={'type': 'date'}),  # Champ date avec le type 'date'
        }


class ReineForm(forms.ModelForm):
    class Meta:
        model = Reine
        fields = ['id_reine', 'rucher', 'age', 'sante', 'date_remplacement']
        widgets = {
            'date_remplacement': forms.DateInput(attrs={'type': 'date'})
        }

class RucherForm(forms.ModelForm):
    class Meta:
        model = Rucher
        fields = ['nom', 'emplacement', 'date_creation']
        widgets = {
            'date_creation': forms.DateInput(attrs={'type': 'date'})
        }

