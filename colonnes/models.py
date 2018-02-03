from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
        utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
        nom_tag = models.CharField(max_length=30, blank=False, help_text = "Entrez un Tag")

        def __str__(self):              # __unicode__ on Python 2
            return self.nom_tag

class Emotion(models.Model):
<<<<<<< HEAD
        utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
        statut_emo = models.CharField(max_length=30, blank=False, help_text = "Non de l'émotion")

        def __str__(self):              # __unicode__ on Python 2
            return self.statut_emo
=======
        statut_emo = models.CharField(max_length=30, blank=False, help_text = "Nom de l'émotion")
        def __str__(self):              # __unicode__ on Python 2
            return '%s' % (self.statut_emo)


class Emotion_Colonne(models.Model):
        emo = models.ForeignKey(Emotion, on_delete=models.CASCADE)
        intensite = models.IntegerField(max_length=1, default='5')
        def __str__(self):
                return '%s %s' % (self.emo, self.intensite)
>>>>>>> 99e5acd438f5413d8f072b0da6d891f808753d4b

class Colonne(models.Model):

        EMOTIONS = (
        ('JO','Joie'),
        ('CO','Colère'),
        ('TR','Tristesse'),
        ('DE','Dégoût'),
        ('PE','Peur'),
        )

        INTENSITE = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
        )

        utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
        situation = models.TextField(max_length=1000, blank=False, help_text = "Décrivez la Situation")
        pensee_aut = models.TextField(max_length=500, blank=False, help_text = "Pensée automatique")
<<<<<<< HEAD
        pensee_alt = models.TextField(max_length=500, blank=False, help_text = "Pensée alternative")
=======
        emo_aut = models.ManyToManyField(Emotion_Colonne, related_name='%(class)s_automatique')
        pensee_alt = models.TextField(max_length=500, blank=False, help_text = "Pensée alternative")
        emo_alt = models.ManyToManyField(Emotion_Colonne, related_name='%(class)s_alternative')
>>>>>>> 99e5acd438f5413d8f072b0da6d891f808753d4b
        date_ajout = models.DateTimeField(auto_now=True, help_text = "Date de l'ajout") #prend la date et l'heure en même temps
        date_event = models.DateTimeField(auto_now=False, help_text = "Date de l'événement")
        tag = models.ManyToManyField(Tag)
        emotion = models.CharField(null=False, max_length=2, default="JO", choices=EMOTIONS)
        intensiteAut = models.IntegerField(default=5, choices=INTENSITE)
        intensiteAlt = models.IntegerField(default=5, choices=INTENSITE)


        def __str__(self):              # __unicode__ on Python 2
            return self.situation

class Conseil(models.Model):

        type_conseil = models.CharField(max_length=30, blank=False, help_text = "Type du conseil")
        contenu_conseil = models.CharField(max_length=400, blank=False, help_text = "Contenu du conseil")
        def __str__(self):              # __unicode__ on Python 2
            return '%s' % (self.contenu_conseil)


class Lien_Ut_Th(models.Model):
        user = models.ForeignKey(User, related_name='%(class)s_utilisateur', on_delete=models.CASCADE)
        ther = models.ForeignKey(User, related_name='%(class)s_therapeute', on_delete=models.CASCADE)
