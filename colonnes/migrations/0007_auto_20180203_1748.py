# Generated by Django 2.1.dev20180125184051 on 2018-02-03 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colonnes', '0006_lien_ut_th'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emotion_Colonne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensite', models.IntegerField(default='5', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='emotion',
            name='intensite',
        ),
        migrations.AlterField(
            model_name='colonne',
            name='emo_alt',
            field=models.ManyToManyField(related_name='colonne_alternative', to='colonnes.Emotion_Colonne'),
        ),
        migrations.AlterField(
            model_name='colonne',
            name='emo_aut',
            field=models.ManyToManyField(related_name='colonne_automatique', to='colonnes.Emotion_Colonne'),
        ),
        migrations.AddField(
            model_name='emotion_colonne',
            name='emo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colonnes.Emotion'),
        ),
    ]
