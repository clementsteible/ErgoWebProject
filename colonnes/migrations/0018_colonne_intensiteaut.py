# Generated by Django 2.0 on 2018-02-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colonnes', '0017_remove_colonne_intensite'),
    ]

    operations = [
        migrations.AddField(
            model_name='colonne',
            name='intensiteAut',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1),
        ),
    ]
