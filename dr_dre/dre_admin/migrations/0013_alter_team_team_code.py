# Generated by Django 3.2.6 on 2021-08-19 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dre_admin', '0012_alter_department_dep_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_code',
            field=models.CharField(default='All', max_length=30),
        ),
    ]
