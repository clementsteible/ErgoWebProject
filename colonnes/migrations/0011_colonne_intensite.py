# Generated by Django 2.0 on 2018-02-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colonnes', '0010_colonne_emotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='colonne',
            name='intensite',
            field=models.IntegerField(choices=[(1, '1')], default=1),
        ),
    ]
