# Generated by Django 3.2.7 on 2021-10-22 10:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_auto_20211022_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='executant',
            name='date_first_creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de parution'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='executant',
            name='date_last_modification',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de dernière modification'),
        ),
        migrations.AddField(
            model_name='maire',
            name='date_first_creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de parution'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maire',
            name='date_last_modification',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de dernière modification'),
        ),
        migrations.AddField(
            model_name='mairie',
            name='date_first_creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de parution'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mairie',
            name='date_last_modification',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de dernière modification'),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_first_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('executant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Client.executant', verbose_name='Executant')),
                ('maire', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Client.maire', verbose_name='Maire')),
                ('mairie', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Client.mairie', verbose_name='mairie')),
            ],
        ),
    ]
