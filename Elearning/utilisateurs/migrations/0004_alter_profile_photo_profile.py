# Generated by Django 4.1.6 on 2023-02-11 13:54

from django.db import migrations, models
import utilisateurs.models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0003_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo_profile',
            field=models.ImageField(blank=True, upload_to=utilisateurs.models.renommer_image),
        ),
    ]