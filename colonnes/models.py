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
    prenom1 = models.CharField(max_length=30, blank=False, help_text = "Prénom")
    prenom2 = models.CharField(max_length=30, help_text = "Deuxième Prénom")
    date_de_naissance = models.CharField(max_length=8, blank=False, help_text = "Date de Naissance")
    pays = models.CharField(max_length=30, blank=False, help_text = "Pays de Résidence")
    ville = models.CharField(max_length=30, help_text = "Ville")
    langue = models.CharField(max_length=30, help_text = "Nom")
    adresse_mail = models.EmailField(max_length=254, blank=False, help_text = "Nom")