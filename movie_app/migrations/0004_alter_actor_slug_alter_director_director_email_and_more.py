# Generated by Django 4.0.4 on 2022-06-24 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_actor_slug_alter_actor_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='director',
            name='director_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='director',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
