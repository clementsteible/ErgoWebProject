from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from colonnes.models import Colonne, Tag, Emotion, Statistiques
from colonnes.forms import ColonneForm, AjoutTagForm, AjoutEmotionForm, StatistiquesForm, EnvoieMailForm
from .forms import SignUpForm
from django.shortcuts import redirect
from matplotlib import pyplot as PLT
from io import BytesIO, StringIO
import PIL
from PIL import Image
import pylab
import numpy as NP
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import send_mail

# Create your views here.

def deverouillage(request):
    return render(request, 'colonnes/deverouillage.html', {})

def nouvelle_entree(request):
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
        #On instancie les variables globales:
            #Les dates
        dateDebut = datetime.now()
        dateFin = datetime.now()
            #Les colonnes de l'utilisateur connecté
        colPeriode = Colonne.objects.filter(utilisateur=request.user)
            #Une variable String à vide
        emotionStats =''
            #Une liste contenant les codes ""émotions", ces codes correspondent respectivement à : Joie, Peur, Tristess, Colère, Dégoût
        listeEmotion = ["JO",'PE',"TR","CO","DE"]

        if request.method == "POST":
            formStatistiques = StatistiquesForm(request.POST)
            if formStatistiques.is_valid():
                stats = formStatistiques.save(commit=False)
                #On sauvegarde le temps de récupérer les valeurs des champs
                stats.save()
                #On récupère la date de début du formulaire
                dateDebut = stats.dateDeDebut
                #Comme l'heure est initialisée à minuit on récupère la date de fin du formulaire et on lui ajoute un jour
                dateFin = stats.dateDeFin + timedelta(days=1)
                #On récupère la valeur du champ émotion
                emotionStats = stats.emotion
                #On supprime directement les valeurs dans la base de données pour ne pas créer de conflits potentiels futurs
                stats.delete()
                #... puis on récupère les colonnes ayant une date contenue entre la date de début et la date de fin entrées dans le formulaire
                colPeriode = Colonne.objects.filter(date_event__range=(dateDebut,dateFin))
                #Si l'utilisateur a choisi l'option 'Toutes' pour le champ 'Émotion' du formulaire nous allons lui afficher les moyennes les intensités respectivement pour chacune des émotions
                if emotionStats == 'TO':
                    #On récupère toutes les queryset des colonnes pour chaque Emotion :
                        #On délcare un compteur qui servira à parcourir la liste
                    i=0
                        #Pour chaque élément de la liste on instancie les colonnes de l'utilisateur contenant tles émotions respectives
                    for emotions in listeEmotion:
                        listeEmotion[i] = colPeriode.filter(emotion__contains=emotions)
                        i=i+1

                    nbrCO = listeEmotion[3].count()


                    return render(request, 'colonnes/statistiques.html', {'nbrCO':nbrCO,'listeEmotion':listeEmotion, 'colPeriode':colPeriode, 'dateDebut':dateDebut,'dateFin':dateFin, 'emotionStats':emotionStats, 'formStatistiques':formStatistiques})

            return render(request, 'colonnes/statistiques.html', {'listeEmotion':listeEmotion, 'colPeriode':colPeriode, 'dateDebut':dateDebut,'dateFin':dateFin, 'emotionStats':emotionStats, 'formStatistiques':formStatistiques})

        else :
            formStatistiques = StatistiquesForm()
            return render(request, 'colonnes/statistiques.html', {'listeEmotion':listeEmotion, 'colPeriode':colPeriode, 'dateDebut':dateDebut,'dateFin':dateFin, 'emotionStats':emotionStats, 'formStatistiques':formStatistiques})

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

def envoiemail(request):
    if request.method == 'POST':
        formEnvoieMail = EnvoieMailForm(request.POST)
        if formEnvoieMail.is_valid():
            subject = formEnvoieMail.cleaned_data['objet']
            message = formEnvoieMail.cleaned_data['situation']
            sender = formEnvoieMail.cleaned_data['votre_email']
            recipients = formEnvoieMail.cleaned_data['email_therapeute']
            send_mail(subject, message, sender, recipients)
            return render(request, 'colonnes/parametres.html', {})
    else :
        formEnvoieMail = EnvoieMailForm()
    return render(request, 'colonnes/envoiemail.html', {'formEnvoieMail': formEnvoieMail})
