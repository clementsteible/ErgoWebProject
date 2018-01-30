from django.urls import path
from . import views

urlpatterns = [
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
]
