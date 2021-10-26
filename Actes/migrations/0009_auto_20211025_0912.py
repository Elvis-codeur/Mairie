# Generated by Django 3.2.2 on 2021-10-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actes', '0008_auto_20211022_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actesdecesmodel',
            name='dresse_le_age',
            field=models.IntegerField(default=0, verbose_name='Dressé âges'),
        ),
        migrations.AlterField(
            model_name='actesdecesmodel',
            name='dresse_le_heure',
            field=models.IntegerField(default=0, verbose_name='Dressé le (minutes)'),
        ),
        migrations.AlterField(
            model_name='actesdecesmodel',
            name='dresse_le_minutes',
            field=models.IntegerField(default=0, verbose_name='Dressé le (minutes)'),
        ),
        migrations.AlterField(
            model_name='actesnaissancemodel',
            name='dresse_le_age',
            field=models.IntegerField(default=0, verbose_name='Dressé âges'),
        ),
        migrations.AlterField(
            model_name='actesnaissancemodel',
            name='dresse_le_heure',
            field=models.IntegerField(default=0, verbose_name='Dressé le (minutes)'),
        ),
        migrations.AlterField(
            model_name='actesnaissancemodel',
            name='dresse_le_minutes',
            field=models.IntegerField(default=0, verbose_name='Dressé le (minutes)'),
        ),
        migrations.AlterField(
            model_name='actesnaissancemodel',
            name='heure',
            field=models.IntegerField(default=0, verbose_name='heure(s)'),
        ),
        migrations.AlterField(
            model_name='actesnaissancemodel',
            name='minute',
            field=models.IntegerField(default=0, verbose_name='minute(s)'),
        ),
    ]