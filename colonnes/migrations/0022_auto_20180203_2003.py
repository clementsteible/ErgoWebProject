# Generated by Django 2.0 on 2018-02-03 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colonnes', '0021_auto_20180203_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='nom_tag',
            field=models.CharField(help_text='Entrez un Tag', max_length=30),
        ),
    ]
