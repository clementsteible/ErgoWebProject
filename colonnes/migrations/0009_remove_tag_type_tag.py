# Generated by Django 2.0 on 2018-02-03 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colonnes', '0008_auto_20180203_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='type_tag',
        ),
    ]
