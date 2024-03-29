# Generated by Django 3.2.7 on 2021-11-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actes', '0010_auto_20211029_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='actesdecesmodel',
            name='acte_numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actesdecesmodel',
            name='annee',
            field=models.IntegerField(default=2021),
        ),
        migrations.AddField(
            model_name='actesdecesmodel',
            name='feillet_numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actesdecesmodel',
            name='registre_numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actesdecesmodel',
            name='volet_numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actesmariagemodel',
            name='acte_numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actesmariagemodel',
            name='annee',
            field=models.IntegerField(default=2021),
        ),
        migrations.AddField(
            model_name='actesmariagemodel',
            name='feillet_numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actesmariagemodel',
            name='registre_numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actesmariagemodel',
            name='volet_numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actesnaissancemodel',
            name='acte_numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actesnaissancemodel',
            name='annee',
            field=models.IntegerField(default=2021),
        ),
        migrations.AddField(
            model_name='actesnaissancemodel',
            name='feillet_numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actesnaissancemodel',
            name='registre_numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actesnaissancemodel',
            name='volet_numero',
            field=models.IntegerField(default=0),
        ),
    ]
