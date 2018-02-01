from django.contrib import admin
from .models import Personne
from .models import Colonne
from .models import Emotion
from .models import Tag
from .models import Conseil

#Importation du modèle Personne (Utilisateur/Thérapeute) dans l'interface admin de Django
admin.site.register(Personne)
#Importation du modèle Colonne
admin.site.register(Colonne)
#Importation du modèle Emotion
admin.site.register(Emotion)
#Importation du modèle Tag
admin.site.register(Tag)
#Importation du modèle Conseil
admin.site.register(Conseil)

