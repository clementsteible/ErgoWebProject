# Generated by Django 2.0 on 2018-02-03 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colonnes', '0007_remove_emotion_intensite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colonne',
            name='emo_alt',
        ),
        migrations.RemoveField(
            model_name='colonne',
            name='emo_aut',
        ),
    ]