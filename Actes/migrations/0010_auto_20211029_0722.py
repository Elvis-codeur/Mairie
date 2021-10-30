# Generated by Django 3.2.7 on 2021-10-29 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actes', '0009_auto_20211025_0912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actesdecesmodel',
            old_name='scan_manuscrit',
            new_name='original',
        ),
        migrations.RenameField(
            model_name='actesnaissancemodel',
            old_name='scan_manuscrit',
            new_name='original',
        ),
        migrations.RemoveField(
            model_name='actesmariagemodel',
            name='scan_manuscrit',
        ),
        migrations.AddField(
            model_name='actesdecesmodel',
            name='transcription',
            field=models.FileField(default='', upload_to='actes_deces_transcription/'),
        ),
        migrations.AddField(
            model_name='actesmariagemodel',
            name='original',
            field=models.FileField(default='', upload_to='actes_mariage_original/'),
        ),
        migrations.AddField(
            model_name='actesmariagemodel',
            name='transcription',
            field=models.FileField(default='', upload_to='actes_mariage_transcription/'),
        ),
        migrations.AddField(
            model_name='actesnaissancemodel',
            name='transcription',
            field=models.FileField(default='', upload_to='actes_naissance_transcription/'),
        ),
    ]