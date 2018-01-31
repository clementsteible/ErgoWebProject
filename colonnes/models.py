from django.db import models
from django.utils import timezone

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
    nom = models.CharField(max_length=30, blank=False, help_text = "Nom")
    prenom = models.CharField(max_length=30, default='', blank=False, help_text = "Prénom")
    date_de_naissance = models.CharField(max_length=8, blank=False, help_text = "Date de Naissance")
    pays = models.CharField(max_length=30, blank=False, help_text = "Pays de Résidence")
    ville = models.CharField(max_length=30, help_text = "Ville")
    langue = models.CharField(max_length=30, help_text = "Nom")
    adresse_mail = models.EmailField(max_length=254, blank=False)
    mot_de_passe = models.CharField(max_length=30, default='')
    def __str__ (self):
        return '%s %s' % (self.prenom1, self.nom)


"""

class Colonne(models.model):

        situation = models.TextField(max_length=30, blank=False, help_text = "Décrivez la Situation")
        pensée_aut = models.TextField(max_length=30, blank=False, help_text = "Nom")
        pensée-alt = models.TextField(max_length=30, blank=False, help_text = "Nom")
        date_ajout = models.CharField(max_length=30, blank=False, help_text = "Nom")
        horaire_ajout = models.CharField(max_length=30, blank=False, help_text = "Nom")
        date_event = models.CharField(max_length=30, blank=False, help_text = "Nom")
        horaire_event = models.CharField(max_length=30, blank=False, help_text = "Nom")
        id_ut = models.CharField(max_length=30, blank=False, help_text = "Nom")

class Emotion(models.model):

        id_col = models.CharField(max_length=30, blank=False, help_text = "Nom")
        id_tag = models.CharField(max_length=30, blank=False, help_text = "Nom")
        statut_emo = models.CharField(max_length=30, blank=False, help_text = "Nom")
        intensite = models.IntegerField(help_text = "Intensité de l'émotion")




class Tag(models.model):

        id_ut = models.CharField(max_length=30, blank=False, help_text = "Nom")
        id_col = models.CharField(max_length=30, blank=False, help_text = "Nom")
        nom_tag = models.CharField(max_length=30, blank=False, help_text = "Entrez un Tag")
        type_tag = models.CharField(max_length=30, blank=False, help_text = "Nom")


 class Lien_tag_colonne(models.model):

        id_tag = models.CharField(max_length=30, blank=False, help_text = "Nom")
        id_col = models.CharField(max_length=30, blank=False, help_text = "Nom")

class Conseil(models.model):

        type_conseil = models.CharField(max_length=30, blank=False, help_text = "Nom")
        contenu_conseil = models.CharField(max_length=30, blank=False, help_text = "Nom")


        """
