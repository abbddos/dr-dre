# Generated by Django 3.2.6 on 2021-08-13 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dre_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]