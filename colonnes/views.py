from django.shortcuts import render
from colonnes.models import Personne
from .forms import InscriptionForm, AuthentificationForm

# Create your views here.

def deverouillage(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'colonnes/deverouillage.html', {})#context)

def nouvelle_entree(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'colonnes/nouvelle_entree.html', {})

def journal(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'colonnes/journal.html', {})

def statistiques(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'colonnes/statistiques.html', {})

def developpement_personnel(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {'latest_question_list': latest_question_list}
    georges_pays = Personne.objects.get(id=1).pays
    context = {'georges_pays': georges_pays}
    return render(request, 'colonnes/developpement_personnel.html', context)

def parametres(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'colonnes/parametres.html', {})


def authentification(request):
    #On ajoute le formulaire d'authentification à la vue
    formAuthentification = AuthentificationForm()
    return render(request, 'colonnes/authentification.html', {'formAuthentification':formAuthentification})

def inscription(request):
    #On ajoute le formulaire d'inscription à la vue
    formInscription = InscriptionForm()
    return render(request, 'colonnes/inscription.html', {'formInscription':formInscription})
