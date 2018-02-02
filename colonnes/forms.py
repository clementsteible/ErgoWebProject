from django import forms
from .models import Personne
from .models import Colonne

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ('nom', 'prenom', 'date_de_naissance', 'pays', 'ville', 'langue', 'adresse_mail','mot_de_passe',)

class AuthentificationForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ('adresse_mail','mot_de_passe',)
