from django.contrib import admin
from .models import Colonne, Emotion, Tag, Conseil, Statistiques
from .models import Lien_Ut_Th

#Importation du modèle Colonne
admin.site.register(Colonne)
#Importation du modèle Emotion
#admin.site.register(Emotion)
#Importation du modèle Tag
admin.site.register(Tag)
#Importation du modèle Conseil
admin.site.register(Conseil)
#Importation du modèle pour le lien utilisateur thérapeute
admin.site.register(Lien_Ut_Th)
#Importation du modèle Statistiques
admin.site.register(Statistiques)
