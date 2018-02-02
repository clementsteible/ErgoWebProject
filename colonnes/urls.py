from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #Page de login
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
    #Page pour les conseils de développement personnel
    path('developpement_personnel/', views.developpement_personnel, name='developpement_personnel'),
    #Page des paramètres de l'application
    path('parametres/', views.parametres, name='parametres'),
    #Page d'authentification
    path('authentification/', views.authentification, name='authentification'),
    #Page d'authentification
    path('inscription/', views.inscription, name='inscription'),
    #Showimage
    path('showimage/', views.showimage, name='showimage'),

]
