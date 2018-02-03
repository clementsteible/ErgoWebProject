from django import forms
from .models import Personne, Colonne, Emotion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

"""
class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ('nom', 'prenom', 'date_de_naissance', 'pays', 'ville', 'langue', 'adresse_mail','mot_de_passe',)

class AuthentificationForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ('adresse_mail','mot_de_passe',)

        from django import forms
"""

class ColonneForm(forms.ModelForm):
    CHOICES = "("
    #nb_emotions = Emotion.objects.count()
    #i=0;
    for e in Emotion.objects.all() :
           # emo = Emotion.objects.all()[:1].get()
           # i += 1
           CHOICES += "(" + str(e.statut_emo) + ", '" + str(e.statut_emo) + "'),"
    CHOICES += ")"
    #ne marche pas alors que la structure de CHOICES correspond normalement à ce qui est attendu
    #emotion_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = Colonne
        fields = ('situation', 'pensee_aut', 'emo_aut', "pensee_alt", "emo_alt","date_event","tag")

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
