# Generated by Django 2.0 on 2018-02-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colonnes', '0013_auto_20180203_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colonne',
            name='intensite',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (10, '10')], default=1),
        ),
    ]
