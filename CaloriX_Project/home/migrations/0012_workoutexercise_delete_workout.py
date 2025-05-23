# Generated by Django 5.1.6 on 2025-03-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_workout'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('benefits', models.TextField()),
                ('age_limit', models.CharField(max_length=50)),
                ('process', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
