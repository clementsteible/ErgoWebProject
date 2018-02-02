from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

"""
 # utilisateur(id_ut, statut, nom, prénom1, prénom2, date_de_naissance, pays, ville, langue, adresse_mail)

# Colonne(id_col, situation, pensée_aut, pensée-alt, date_ajout, horaire_ajout, date_event, horaire_event, id_ut)

# Emotion(id_emo, id_col, id_tag, statut_emo, intensite)

# Tag(id_tag, id_ut, id_col, nom_tag, type_tag)

# lientc(id_lientc, id_tag, id col)

# Conseil(type_conseil, contenu_conseil)
"""

class Personne(models.Model):

    UTILISATEUR = 'UT'
    THERAPEUTE = 'TH'
    STATUT_CHOICES = (
        (UTILISATEUR, 'Utilisateur'),
        (THERAPEUTE, 'Therapeute'),
    )
    statut = models.CharField(
        max_length=2,
        choices = STATUT_CHOICES,
        default = UTILISATEUR,
    )
    lien_therapeute = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30, default='')
    date_de_naissance = models.DateField(auto_now=False, auto_now_add=False,)
    pays = models.CharField(max_length=30)
    ville = models.CharField(max_length=30)
    langue = models.CharField(max_length=30)
    adresse_mail = models.EmailField(max_length=254)
    mot_de_passe = models.CharField(max_length=30, default='')
    def __str__ (self):
        return '%s %s' % (self.prenom, self.nom)

class Tag(models.Model):

        nom_tag = models.CharField(max_length=30, blank=False, help_text = "Entrez un Tag")
        type_tag = models.CharField(max_length=30, blank=False, help_text = "Famille du tag")
        def __str__(self):              # __unicode__ on Python 2
            return self.nom_tag

class Emotion(models.Model):
        statut_emo = models.CharField(max_length=30, blank=False, help_text = "Non de l'émotion")
        intensite = models.IntegerField(help_text = "Intensité de l'émotion")

        def __str__(self):              # __unicode__ on Python 2
            return '%s %s' % (self.statut_emo, self.intensite)

class Colonne(models.Model):

        personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
        situation = models.TextField(max_length=1000, blank=False, help_text = "Décrivez la Situation")
        pensee_aut = models.TextField(max_length=500, blank=False, help_text = "Pensée automatique")
        emo_aut = models.ManyToManyField(Emotion, related_name='%(class)s_automatique')
        pensee_alt = models.TextField(max_length=500, blank=False, help_text = "Pensée alternative")
        emo_alt = models.ManyToManyField(Emotion, related_name='%(class)s_alternative')
        date_ajout = models.DateTimeField(auto_now=True, help_text = "Date de l'ajout") #prend la date et l'heure en même temps
        date_event = models.DateTimeField(auto_now=False, help_text = "Date de l'événement")
        tag = models.ManyToManyField(Tag)

        def __str__(self):              # __unicode__ on Python 2
            return self.situation

"""
class Lien_Emotion_Colonne(models.Model):
        ALTERNATIVE = 'AL'
        RESSENTIE = 'RE'
        TYPE_EMOTION_CHOIX = (
            (ALTERNATIVE, 'Alternative'),
            (RESSENTIE, 'Ressentie'),
        )
        type_emotion = models.CharField(
            max_length=2,
            choices=TYPE_EMOTION_CHOIX,
            default=RESSENTIE,
        )
        colonne = models.ForeignKey(Colonne, on_delete=models.CASCADE)
        emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)

class Lien_Tag_Colonne(models.Model):
        tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
        col = models.ForeignKey(Colonne, on_delete=models.CASCADE)

"""
class Conseil(models.Model):

        type_conseil = models.CharField(max_length=30, blank=False, help_text = "Type du conseil")
        contenu_conseil = models.CharField(max_length=400, blank=False, help_text = "Contenu du conseil")
        def __str__(self):              # __unicode__ on Python 2
            return '%s' % (self.contenu_conseil)

"""
class Lien_Ut_Th(models.Model):
        user = models.ForeignKey(Personne, on_delete=models.CASCADE)
        ther = models.ForeignKey(Personne, on_delete=models.CASCADE)
"""
