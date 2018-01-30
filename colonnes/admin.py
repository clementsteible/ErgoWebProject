from django.contrib import admin
from .models import Personne

#Importation du modèle Personne (Utilisateur/Thérapeute) dans l'interface admin de Django
admin.site.register(Personne)
