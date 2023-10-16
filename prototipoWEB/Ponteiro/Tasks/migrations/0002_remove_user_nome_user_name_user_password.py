# Generated by Django 4.2.6 on 2023-10-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nome',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.TextField(default='admin', max_length=80),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.TextField(default='admin', max_length=20),
        ),
    ]