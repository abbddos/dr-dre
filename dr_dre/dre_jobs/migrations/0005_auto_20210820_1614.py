# Generated by Django 3.2.6 on 2021-08-20 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dre_admin', '0013_alter_team_team_code'),
        ('dre_jobs', '0004_alter_job_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dre_jobs.customer'),
        ),
        migrations.AlterField(
            model_name='job',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dre_admin.department'),
        ),
    ]
