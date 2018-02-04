from django import forms
from .models import Colonne, Tag, Emotion, Statistiques
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

class StatistiquesForm(forms.ModelForm):
    class Meta:
        model = Statistiques
        fields = ('dateDeDebut', 'dateDeFin', 'emotion')

class ColonneForm(forms.ModelForm):
    class Meta:
        model = Colonne
        fields = ('situation', 'pensee_aut', 'emotion', 'intensiteAut', "pensee_alt", 'intensiteAlt', "date_event",'tag')

class AjoutTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('nom_tag',)

class AjoutEmotionForm(forms.ModelForm):
    class Meta:
        model = Emotion
        fields = ('statut_emo',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
