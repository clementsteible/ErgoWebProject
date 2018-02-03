from django.shortcuts import render
<<<<<<< HEAD
from colonnes.models import Colonne, Tag
from colonnes.forms import ColonneForm, AjoutTagForm, AjoutEmotionForm
=======
from colonnes.models import Personne, Colonne, Emotion
from colonnes.forms import ColonneForm
>>>>>>> 99e5acd438f5413d8f072b0da6d891f808753d4b
from .forms import SignUpForm
from django.shortcuts import redirect
from matplotlib import pyplot as PLT
import numpy as NP
from io import BytesIO, StringIO
import PIL
import pylab
from PIL import Image
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def deverouillage(request):
    return render(request, 'colonnes/deverouillage.html', {})

def nouvelle_entree(request):
    """
    CHOICES = "("
    for e in Emotion.objects.all() :
           CHOICES += "(" + str(e.statut_emo) + ", '" + str(e.statut_emo) + "'),"
    CHOICES += ")"
    return HttpResponse(CHOICES)
    """
    if request.method == "POST":
        formColonne = ColonneForm(request.POST)
        if formColonne.is_valid():
            colonne = formColonne.save(commit = False)
            colonne.utilisateur = request.user
            colonne.save()
            messageEnregistrementColonneValide = "Votre colonne a bien été enregistrée."
            return render(request, 'colonnes/nouvelle_entree.html',  {'messageEnregistrementColonneValide':messageEnregistrementColonneValide, 'formColonne': formColonne})
    else :
        #On ajoute le formulaire de colonne et d'ajout de tag à la vue
        formColonne = ColonneForm()
        return render(request, 'colonnes/nouvelle_entree.html', {'formColonne': formColonne})

def journal(request):
    return render(request, 'colonnes/journal.html', {})

def statistiques(request):
    return render(request, 'colonnes/statistiques.html', {})
"""
def statistiques(request, periode, emotion):

    if (periode == "jour"){
            periode_jour = timezone.now().day;
            emotions_du_jour =  join Emotion.objects.get(contains
    }

    elif (periode == "semaine"){
        periode_semaine = timezone.now().week;
    }

    elif (periode == "mois"){
        periode_mois = timezone.now().month;
    }

    return render(request, 'colonnes/statistiques.html', {})
"""
def developpement_personnel(request):
    return render(request, 'colonnes/developpement_personnel.html', {})

def parametres(request):
    if request.method == "POST":
        formTag = AjoutTagForm(request.POST)
        if formTag.is_valid():
            tag = formTag.save(commit = False)
            tag.utilisateur = request.user
            tag.save()
            messageEnregistrementTagValide = "Votre nouveau Tag a bien été enregistré."
            return render(request, 'colonnes/parametres.html',  {'formTag':formTag})
    else :
        #On ajoute le formulaire d'ajout de tag à la vue
        formTag = AjoutTagForm()
    return render(request, 'colonnes/parametres.html', {'formTag':formTag})

def showimage(request):
    # je récupère la personne
    #per = Personne.objects.get(id=1)
    #col = per.colonne_set.get(id=1)
    #emo = col.emo_aut.filter(statut_emo='Joie')
    #return HttpResponse(emo)
    periode = '30 derniers jours'
    emotion = 'la Peur '
    # Construct the graph
    t = NP.arange(0.0, 2.0, 0.01)
    s = NP.sin(2*NP.pi*t)
    PLT.plot(t, s, linewidth=1.0)

    PLT.xlabel("Date des entrées de "+ emotion)
    PLT.ylabel("Intensité de "+ emotion)
    PLT.title("Evolution de l'intensité de " + emotion + "sur les " + periode)
    PLT.grid(True)

    # Store image in a string buffer
    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    statistiques = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    statistiques.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")

def login(request):
 #On ajoute le formulaire d'authentification à la vue
    return render(request, 'colonnes/login.html',{})

def logout(request):
    return render(request, 'colonnes/logged_out.html',{})

def signup(request):
    if request.method == 'POST':
        formSignUp = SignUpForm(request.POST)
        if formSignUp.is_valid():
            formSignUp.save()
            return render(request, 'colonnes/login.html',{})
    else:
        formSignUp = SignUpForm()
    return render(request, 'colonnes/signup.html', {'formSignUp': formSignUp})

"""
def inscription(request):
    formAuthentification = AuthentificationForm()
    if request.method == "POST":
        formInscription = InscriptionForm(request.POST)
        if formInscription.is_valid():
            personne = formInscription.save(commit=False)
            personne.save()
            return render(request, 'colonnes/authentification.html',  {'formAuthentification':formAuthentification})
    else :
        #On ajoute le formulaire d'inscription à la vue
        formInscription = InscriptionForm(request.POST)
    return render(request, 'colonnes/inscription.html', {'formInscription':formInscription})

def authentification(request):
    #On ajoute le formulaire d'authentification à la vue
    formAuthentification = AuthentificationForm()
    return render(request, 'colonnes/authentification.html', {'formAuthentification':formAuthentification})
"""
