# Generated by Django 3.2.6 on 2021-08-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dre_admin', '0004_auto_20210818_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dep_description',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
