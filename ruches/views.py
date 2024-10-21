from django.shortcuts import render, get_object_or_404, redirect
from .models import Ruche, Reine, Recolte, Rucher
from .forms import RucheForm, ReineForm, RecolteForm, RucherForm


def home(request):
    return render(request, 'ruches/home.html')



def liste_ruches(request):
    ruches = Ruche.objects.all()
    return render(request, 'ruches/liste_ruches.html', {'ruches': ruches})

def ajouter_ruche(request):
    if request.method == 'POST':
        form = RucheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_ruches')
    else:
        form = RucheForm()
    return render(request, 'ruches/ajout_ruches.html', {'form': form})


def modifier_ruche(request):
    ruches = Ruche.objects.all()

    if request.method == 'POST':
        for ruche in ruches:
            ruche.nom = request.POST.get(f'nom_{ruche.id}', ruche.nom)
            ruche.rucher.nom = request.POST.get(f'rucher_nom_{ruche.id}')
            
            id_reine = request.POST.get(f'id_reine_{ruche.id}')
            if id_reine:
                # Chercher l'instance de Reine avec le nom donné, ou utiliser l'id selon ton modèle
                ruche.id_reine = get_object_or_404(Reine, id_reine=id_reine)  # Ou un autre champ unique comme l'id
            ruche.niveaux_miel = request.POST.get(f'niveaux_miel_{ruche.id}', ruche.niveaux_miel)
            ruche.niveaux_miel = request.POST.get(f'niveaux_miel_{ruche.id}', ruche.niveaux_miel)
            ruche.save()
        return redirect('liste_ruches')
    return render(request, 'ruches/modifier_ruche.html', {'ruches': ruches})


def modifier_reine(request):
    reines = Reine.objects.all()

    if request.method == 'POST':
        for reine in reines:
            reine.id_reine = request.POST.get(f'id_reine_{reine.id_reine}', reine.id_reine)
            reine.rucher.nom = request.POST.get(f'rucher_nom_{reine.id_reine}')
            reine.age = request.POST.get(f'age_{reine.id_reine}', reine.age)
            reine.sante = request.POST.get(f'sante_{reine.id_reine}', reine.sante)
            reine.date_remplacement = request.POST.get(f'date_remplacement_{reine.id_reine}', reine.date_remplacement)

            # Sauvegarder les modifications
            reine.save()

        return redirect('liste_reines')

    return render(request, 'ruches/modifier_reine.html', {'reines': reines})


from django.shortcuts import render, redirect
from .models import Reine
from .forms import ReineForm  # Assure-toi d'avoir un formulaire pour le modèle Reine

def ajouter_reine(request):
    if request.method == 'POST':
        form = ReineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_reines')  # Redirige vers la liste des reines après l'ajout
    else:
        form = ReineForm()

    return render(request, 'ruches/ajout_reines.html', {'form': form})


def liste_reines(request):
    reines = Reine.objects.all()
    return render(request, 'ruches/liste_reines.html', {'reines': reines})

def exploitation_global(request):
    return render(request, 'ruches/global.html')


def liste_ruchers(request):
    ruchers = Rucher.objects.all()
    return render(request, 'ruches/liste_ruchers.html', {'ruchers': ruchers})



def ajouter_rucher(request):
    if request.method == 'POST':
        form = RucherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_ruchers')  
    else:
        form = RucherForm()

    return render(request, 'ruches/ajout_ruchers.html', {'form': form})


def modifier_rucher(request):
    ruchers = Rucher.objects.all()
    if request.method == 'POST':
        for rucher in ruchers:
            rucher.nom = request.POST.get(f'nom_{rucher.id}', rucher.nom)
            rucher.emplacement = request.POST.get(f'emplacement_{rucher.id}', rucher.emplacement)
            rucher.date_creation = request.POST.get(f'date_creation_{rucher.id}', rucher.date_creation)
            # Sauvegarder les modifications
            rucher.save()
        return redirect('liste_ruchers')
    return render(request, 'ruches/modifier_rucher.html', {'ruchers': ruchers})


def liste_recolte(request):
    recoltes = Recolte.objects.all()  # Récupération de toutes les récoltes
    return render(request, 'ruches/liste_recolte.html', {'recoltes': recoltes})

def modifier_recolte(request):
    recoltes = Recolte.objects.all()
    if request.method == 'POST':
        for recolte in recoltes:
            recolte.date_recolte = request.POST.get(f'date_recolte_{recolte.id}', recolte.date_recolte)

            # Récupérer la ruche en fonction du nom fourni
            ruche_nom = request.POST.get(f'ruche_nom_{recolte.id}', recolte.ruche.nom)
            try:
                ruche = Ruche.objects.get(nom=ruche_nom)  # Associer la ruche par son nom
                recolte.ruche = ruche
            except Ruche.DoesNotExist:
                pass  # Gérer le cas où le nom de la ruche n'existe pas

            recolte.quantite_miel = request.POST.get(f'quantite_miel_{recolte.id}', recolte.quantite_miel)
            recolte.save()
        return redirect('liste_recolte')
    return render(request, 'ruches/modifier_recolte.html', {'recoltes': recoltes})

def ajouter_recolte(request):
    if request.method == 'POST':
        form = RecolteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_recolte')  
    else:
        form = RecolteForm()

    return render(request, 'ruches/ajout_recolte.html', {'form': form})













import plotly.express as px
import pandas as pd
from django.shortcuts import render
from .models import Recolte

def graphique_recolte(request):
    # Récupérer toutes les récoltes
    recoltes = Recolte.objects.all()

    # Extraire les données pour les dates et quantités de miel
    dates = [recolte.date_recolte for recolte in recoltes]
    quantites = [recolte.quantite_miel for recolte in recoltes]
    ruches = [recolte.ruche.nom for recolte in recoltes]

    # Créer un graphique à partir des données avec Plotly
    fig = px.line(x=dates, y=quantites, color=ruches, labels={'x': 'Date', 'y': 'Quantité de miel (kg)'}, title="Quantité de miel récoltée par ruche")
    
    # Convertir le graphique en HTML
    graph_html = fig.to_html(full_html=False)

    # Passer le graphique au template
    return render(request, 'ruches/graphique.html', {'graph_html': graph_html})
