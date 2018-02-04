from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#définition des URLS et des views pour chaque url
urlpatterns = [
    #Page de login. j'utilise l'authentification inclue dans Django 
    path('login/', auth_views.LoginView.as_view(template_name='colonnes/login.html'), name='login'),
    #Page de logout
    path('logout/', auth_views.LogoutView.as_view(template_name='colonnes/logged_out.html'), name='logout'),
    #Menu principal de l'application web
    path('', views.deverouillage, name='deverouillage'),
    #Page permettant d'ajouter une nouvelle situation complète
    path('nouvelle_entree/', views.nouvelle_entree, name='nouvelle_entree'),
    #Page Journal, permet de consulter les colonnes de Beck déjà complétées
    path('journal/', views.journal, name='journal'),
    #Page des statistiques
    path('statistiques/', views.statistiques, name='statistiques'),
    #Page des statistiques sur les émotions du jour/semaine/mois
    path('statistiques/<str:periode>/<str:emotion>/', views.statistiques, name='statistiques'),
    #Page pour les conseils de développement personnel
    path('developpement_personnel/', views.developpement_personnel, name='developpement_personnel'),
    #Page des paramètres de l'application
    path('parametres/', views.parametres, name='parametres'),
    #Showimage
    path('showimage/', views.showimage, name='showimage'),
    #Page d'identification
    path('signup/', views.signup, name='signup'),
    #Page d'envoie de mail
    path('envoiemail/', views.envoiemail, name='envoiemail'),
]
