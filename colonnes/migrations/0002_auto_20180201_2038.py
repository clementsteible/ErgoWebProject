# Generated by Django 2.1.dev20180125184051 on 2018-02-01 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colonnes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personne',
            name='lien_therapeute',
        ),
        migrations.AddField(
            model_name='personne',
            name='lien_therapeute',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='colonnes.Personne'),
            preserve_default=False,
        ),
    ]