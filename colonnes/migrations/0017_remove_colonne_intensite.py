# Generated by Django 2.0 on 2018-02-03 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colonnes', '0016_auto_20180203_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colonne',
            name='intensite',
        ),
    ]
