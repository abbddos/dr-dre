# Generated by Django 3.2.6 on 2021-08-19 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dre_admin', '0009_auto_20210819_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dep_code',
            field=models.CharField(blank=True, default='All', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='dep_description',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='department',
            name='dep_name',
            field=models.CharField(blank=True, default='All', max_length=30),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_code',
            field=models.CharField(blank=True, default='All', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_dep',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='dre_admin.department'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_description',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(blank=True, default='All', max_length=40),
        ),
    ]
