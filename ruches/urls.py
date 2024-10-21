from django.urls import path
from . import views

urlpatterns = [
    path('ruches/', views.liste_ruches, name='liste_ruches'),
    path('ruches/ajouter/', views.ajouter_ruche, name='ajouter_ruche'),
    path('ruches/modifier/', views.modifier_ruche, name='modifier_ruche'),
    # Ajouter des URLs pour les autres vues (reines, recoltes, etc.)
    path('', views.home, name='home'),
    path('modifier_reine/', views.modifier_reine, name='modifier_reine'),
    path('liste_reines/', views.liste_reines, name='liste_reines'),  # Assurez-vous que cette vue est définie pour afficher la liste des reines
    path('ajouter_reine/', views.ajouter_reine, name='ajouter_reine'),
    path('exploitation_global', views.exploitation_global, name='exploitation_global'),
    path('liste_ruchers/', views.liste_ruchers, name='liste_ruchers'),
    path('modifier_rucher/', views.modifier_rucher, name='modifier_rucher'),
    path('ajouter_rucher/', views.ajouter_rucher, name='ajouter_rucher'),
    path('liste_recolte/', views.liste_recolte, name='liste_recolte'),
    path('modifier_recolte/', views.modifier_recolte, name='modifier_recolte'),
    path('ajouter_recolte/', views.ajouter_recolte, name='ajouter_recolte'),
    path('liste_recolte/', views.liste_recolte, name='liste_recolte'),




    path('graphique-recolte/', views.graphique_recolte, name='graphique_recolte'),

]
