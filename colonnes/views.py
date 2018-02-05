from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from colonnes.models import Colonne, Tag, Emotion, Statistiques, Lien_Ut_Th
from colonnes.forms import ColonneForm, AjoutTagForm, AjoutEmotionForm, StatistiquesForm, EnvoieMailForm
from .forms import SignUpForm
from django.shortcuts import redirect
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from io import BytesIO, StringIO
import PIL
from PIL import Image
import pylab
import numpy as np
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.core import mail

# Create your views here.

def deverouillage(request):
    return render(request, 'colonnes/deverouillage.html', {})

# view pour ajouter une nouvelle pensée
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
            #Une liste qui contiendra les QuerySets à trier
        listeDonnees = [0, 0, 0, 0, 0]

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
                        #On instancie une nouvelle liste catégorisant les colonnes selon leur attribut emotion
                    for emotions in listeEmotion:
                        listeDonnees[i] = colPeriode.filter(emotion__contains=emotions)
                        i=i+1

                    nbrCO = listeDonnees[3].count()
                    #On instancie une liste pour chaque émotion, chaque liste contient les
                    colJO = listeDonnees[0]
                    listeJO = list(colJO)

                    colPE = listeDonnees[1]
                    listePE = list(colPE)

                    colTR = listeDonnees[2]
                    listeTR = list(colTR)

                    colCO = listeDonnees[3]
                    listeCO = list(colCO)

                    colDE = listeDonnees[4]
                    listeDE = list(colDE)

                    #On instancie également les variables qui nous serviront pour calculer les moyennes des attributs d'intensités automatique et alternative
                    intAutJO = 0
                    intAltJO = 0

                    intAutPE = 0
                    intAltPE = 0

                    intAutTR = 0
                    intAltTR = 0

                    intAutCO = 0
                    intAltCO = 0

                    intAutDE = 0
                    intAltDE = 0


                    #Pour chaque liste et donc chaque émotion on fait la somme des attributs d'intensité automatique et alternative
                    i=0
                    for elt in listeJO:
                        intAutJO = intAutJO + listeJO[i].intensiteAut
                        intAltJO = intAltJO + listeJO[i].intensiteAlt
                        i = i +1

                    i=0
                    for elt in listePE:
                        intAutPE = intAutPE + listePE[i].intensiteAut
                        intAltPE = intAltPE + listePE[i].intensiteAlt
                        i = i +1

                    i=0
                    for elt in listeTR:
                        intAutTR = intAutTR + listeTR[i].intensiteAut
                        intAltTR = intAltTR + listeTR[i].intensiteAlt
                        i = i +1

                    i=0
                    for elt in listeCO:
                        intAutCO = intAutCO + listeCO[i].intensiteAut
                        intAltCO = intAltCO + listeCO[i].intensiteAlt
                        i = i +1

                    i=0
                    for elt in listeDE:
                        intAutDE = intAutDE + listeDE[i].intensiteAut
                        intAltDE = intAltDE + listeDE[i].intensiteAlt
                        i = i +1

                    #On instancie les variables des moyennes de l'intensité Automatique et Alternative pour les récupérer plus tard
                    moyIntAutJO = 0
                    moyIntAltJO = 0
                    #On compte le nombre d'éléments dans la liste pour calculer la moyenne
                    compteurJO = len(listeJO)
                    #Pour chaque émotion on calcule les moyennes de l'intensite Automatique et Alternative si l'intensite !=0, c'est à dire s'il existe au moins une colonne avec une telle émotion
                    if compteurJO > 0:
                        moyIntAutJO = intAutJO / compteurJO
                        moyIntAltJO = intAltJO / compteurJO

                    moyIntAutPE = 0
                    moyIntAltPE = 0
                    compteurPE = len(listePE)
                    if compteurPE > 0:
                        moyIntAutPE = intAutPE / compteurPE
                        moyIntAltPE = intAltPE / compteurPE

                    moyIntAutTR = 0
                    moyIntAltTR = 0
                    compteurTR = len(listeTR)
                    if compteurTR > 0:
                        moyIntAutTR = intAutTR / compteurTR
                        moyIntAltTR = intAltTR / compteurTR

                    moyIntAutCO = 0
                    moyIntAltCO = 0
                    compteurCO = len(listeCO)
                    if compteurCO > 0:
                        moyIntAutCO = intAutCO / compteurCO
                        moyIntAltCO = intAltCO / compteurCO

                    moyIntAutDE = 0
                    moyIntAltDE = 0
                    compteurDE = len(listeDE)
                    if compteurDE > 0:
                        moyIntAutDE = intAutDE / compteurDE
                        moyIntAltDE = intAltDE / compteurDE


                    #On dessine le graphique avec matplotlib
                    f = plt.figure()
                    aut = [moyIntAutJO,moyIntAutPE,moyIntAutTR,moyIntAutCO,moyIntAutDE]
                    alt = [moyIntAltJO,moyIntAltPE,moyIntAltTR,moyIntAltCO,moyIntAltDE]
                    plt.title('Intensités moyennes pour chaque émotion du : '+ dateDebut.strftime("%d/%m/%Y") + ' au ' + dateFin.strftime("%d/%m/%Y"))
                    plt.ylabel('Intensité Moyenne')
                    plt.ylim(0,10)
                    barWidth = 0.5
                    r1 = range(len(aut))
                    r2 = [x + barWidth for x in r1]
                    b1 = plt.bar(r1, aut, width = barWidth, color = ['red' for i in aut], edgecolor = 'none', linewidth = 2)
                    b2 = plt.bar(r2, alt, width = barWidth, color = ['green' for i in aut], edgecolor = 'none', linewidth = 4)
                    plt.xticks([0.25,1.25,2.25,3.25,4.25], ['Joie', 'Peur', 'Tristesse', 'Colère', 'Dégoût'])
                    plt.legend((b1[0],b2[0]),("Pensée Automatique","Pensée Alternative"))

                    canvas = FigureCanvasAgg(f)
                    response = HttpResponse(content_type='image/png')
                    canvas.print_png(response)
                    matplotlib.pyplot.close(f)

                #return render(request, 'colonnes/statistiques.html', {'moyIntAutJO':moyIntAutJO,'moyIntAltJO':moyIntAltJO,'moyIntAutPE':moyIntAutPE,'moyIntAltPE':moyIntAltPE,'moyIntAutTR':moyIntAltTR,'moyIntAutCO':moyIntAutCO,'moyIntAutDE':moyIntAutDE,'moyIntAltDE':moyIntAltDE,'formStatistiques':formStatistiques})
                return response

            return render(request, 'colonnes/statistiques.html', {'formStatistiques':formStatistiques})

        else :
            formStatistiques = StatistiquesForm()
            return render(request, 'colonnes/statistiques.html', {'formStatistiques':formStatistiques})

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
            connection = mail.get_connection()
            connection.open()
            subject = formEnvoieMail.cleaned_data['objet']
            message = 'Situation : \n ' + formEnvoieMail.cleaned_data['situation'] + '\n Pensée automatique : \n' + formEnvoieMail.cleaned_data['pensée_automatique'] + '\n Pensée alternative : \n' + formEnvoieMail.cleaned_data['pensée_alternative'] + '\n Emotion ressentie :\n' + formEnvoieMail.cleaned_data['emotion_ressentie'] + '\n Intensité automatique : \n' + str(formEnvoieMail.cleaned_data['intensité_automatique']) + '\n Intensité alternative : \n' + str(formEnvoieMail.cleaned_data['intensité_alternative'])
            sender = formEnvoieMail.cleaned_data['votre_email']
            recipients = formEnvoieMail.cleaned_data['email_therapeute']
<<<<<<< HEAD
            email = mail.EmailMessage(subject, message, sender, [recipients])
            connection.send_messages([email])
            connection.close()        
=======
            send_mail(subject, message, sender, recipients)
>>>>>>> 5bcfcf7bfb425c77250d608232dd488b778a1587
            return render(request, 'colonnes/parametres.html', {})
    # sinon si l'utilisateur ne vient pas d'envoyer le formulaire
    else :
        email = request.user.email #je récupère le mail de l'utilisateur
        lien_th_ut = Lien_Ut_Th.objects.get(pati=request.user) #je récupère l'objet du lien entre lui et son thérapeute
        therapeute = lien_th_ut.ther # à partir de l'objet récupéré, je récupère le thérapeute qui est une instance du modèle User
        pensees = Colonne.objects.filter(utilisateur=request.user)
        pensee = pensees[1]
        date_ajout = 'Pensée du ' + str(pensee.date_ajout) 
        formEnvoieMail = EnvoieMailForm(initial ={'votre_email': email, 'email_therapeute': therapeute.email, 'objet': date_ajout, 'situation': pensee.situation,'pensée_automatique': pensee.pensee_aut, 'pensée_alternative': pensee.pensee_alt, 'emotion_ressentie': pensee.emotion,'intensité_automatique': pensee.intensiteAut, 'intensité_alternative' : pensee.intensiteAlt})
    return render(request, 'colonnes/envoiemail.html', {'formEnvoieMail': formEnvoieMail})
