# Generated by Django 2.1.dev20180125184051 on 2018-02-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colonnes', '0003_auto_20180201_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colonne',
            name='pensee_alt',
            field=models.TextField(help_text='Pensée alternative', max_length=300),
        ),
        migrations.AlterField(
            model_name='colonne',
            name='pensee_aut',
            field=models.TextField(help_text='Pensée automatique', max_length=300),
        ),
        migrations.AlterField(
            model_name='colonne',
            name='situation',
            field=models.TextField(help_text='Décrivez la Situation', max_length=100),
        ),
    ]