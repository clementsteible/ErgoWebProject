from django.shortcuts import render
from colonnes.models import Personne
from colonnes.models import Colonne
from .forms import InscriptionForm, AuthentificationForm
from django.shortcuts import redirect
from matplotlib import pyplot as PLT
import numpy as NP
from io import BytesIO, StringIO
import PIL
import pylab
from PIL import Image
from django.http import HttpResponse

# Create your views here.

def deverouillage(request):
    return render(request, 'colonnes/deverouillage.html', {})

def nouvelle_entree(request):
    return render(request, 'colonnes/nouvelle_entree.html', {})

def journal(request):
    return render(request, 'colonnes/journal.html', {})

def statistiques(request):
    return render(request, 'colonnes/statistiques.html', {})

def developpement_personnel(request):
    return render(request, 'colonnes/developpement_personnel.html', {})

def parametres(request):
    return render(request, 'colonnes/parametres.html', {})

def authentification(request):
    #On ajoute le formulaire d'authentification à la vue
    formAuthentification = AuthentificationForm()
    return render(request, 'colonnes/authentification.html', {'formAuthentification':formAuthentification})

def showimage(request):
    # je récupère la personne
    per = Personne.objects.get(id=1)
    col = per.colonne_set.get(id=1)
    emo = col.emo_aut.filter(statut_emo='Joie')
    return HttpResponse(emo)
    # Construct the graph
    t = NP.arange(0.0, 2.0, 0.01)
    s = NP.sin(2*NP.pi*t)
    PLT.plot(t, s, linewidth=1.0)

    PLT.xlabel('time (s)')
    PLT.ylabel('voltage (mV)')
    PLT.title('About as simple as it gets, folks')
    PLT.grid(True)

    # Store image in a string buffer
    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")

def login(request):
 #On ajoute le formulaire d'authentification à la vue
    return render(request, 'colonnes/login.html',{})

def logout(request):
    return render(request, 'colonnes/logged_out.html',{})

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
