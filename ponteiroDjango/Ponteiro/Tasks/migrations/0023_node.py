# Generated by Django 4.2.7 on 2023-11-09 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0022_binarysearchtree_linkedlist_group_adminlist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]