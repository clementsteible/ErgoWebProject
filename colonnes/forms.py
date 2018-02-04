from django import forms
from .models import Colonne, Tag, Emotion, Statistiques, Lien_Ut_Th
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

class EnvoieMailForm(forms.Form):
    """
    
    therapeute = Lien_Ut_Th.objects.filter(pati.first_name=user.first_name)
    patient = forms.CharField(initial=name_patient)
    mail_therapeute = forms.EmailField(initial=therapeute.email)"""
    
    votre_email = forms.EmailField(max_length=254, required=True)
    objet = forms.CharField(max_length=30, required=True)
    email_therapeute = forms.EmailField(max_length=254, required=True)
    situation = forms.CharField(widget=forms.Textarea)
    pensée_automatique= forms.CharField(widget=forms.Textarea)
    pensée_alternative = forms.CharField(widget=forms.Textarea)
    emotion_ressentie = forms.CharField(max_length=2)
    intensité_automatique = forms.IntegerField()
    intensité_alternative = forms.IntegerField()

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
