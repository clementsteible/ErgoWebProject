# Generated by Django 2.0 on 2018-01-31 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colonnes', '0004_auto_20180131_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='adresse_mail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='personne',
            name='date_de_naissance',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='personne',
            name='langue',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='personne',
            name='mot_de_passe',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='personne',
            name='nom',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='personne',
            name='pays',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='personne',
            name='prenom',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='personne',
            name='ville',
            field=models.CharField(max_length=30),
        ),
    ]