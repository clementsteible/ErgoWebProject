from django.shortcuts import render

# Create your views here.

def menu(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'colonnes/menu.html', {})#context)

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
    return render(request, 'colonnes/developpement_personnel.html', {})

def parametres(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'colonnes/parametres.html', {})
