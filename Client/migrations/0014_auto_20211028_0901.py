# Generated by Django 3.2.7 on 2021-10-28 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0013_auto_20211028_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='executant',
            name='grade',
            field=models.CharField(default='Officier', max_length=8),
        ),
        migrations.AddField(
            model_name='maire',
            name='grade',
            field=models.CharField(default='Maire', max_length=5),
        ),
    ]