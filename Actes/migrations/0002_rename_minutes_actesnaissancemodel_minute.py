# Generated by Django 3.2.7 on 2021-10-17 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Actes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actesnaissancemodel',
            old_name='minutes',
            new_name='minute',
        ),
    ]
