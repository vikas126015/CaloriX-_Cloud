# Generated by Django 5.1.6 on 2025-02-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_recoveryinsights_user_hydrationcalorietracker_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hydrationcalorietracker',
            name='weight',
            field=models.FloatField(blank=True, help_text='Enter your weight in kg', null=True),
        ),
    ]
