from django.contrib import admin
#from .models import Personne
from .models import Colonne
from .models import Emotion
from .models import Tag
from .models import Conseil
from .models import Lien_Ut_Th
from .models import Emotion_Colonne

##Importation du modèle Personne (Utilisateur/Thérapeute) dans l'interface admin de Django
#admin.site.register(Personne)
#Importation du modèle Colonne
admin.site.register(Colonne)
#Importation du modèle Emotion
admin.site.register(Emotion)
#Importation du modèle Tag
admin.site.register(Tag)
#Importation du modèle Conseil
admin.site.register(Conseil)
#Importation du modèle pour le lien utilisateur thérapeute
admin.site.register(Lien_Ut_Th)
admin.site.register(Emotion_Colonne)
