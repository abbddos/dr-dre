# Generated by Django 3.2.6 on 2021-08-19 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dre_admin', '0005_auto_20210819_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dep_code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='dep_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_code',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_dep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dre_admin.department'),
        ),
    ]
