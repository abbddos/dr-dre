# Generated by Django 3.2.6 on 2021-08-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dre_jobs', '0003_alter_customer_registerdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]