# Generated by Django 5.1.4 on 2024-12-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_picture_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='profile_covers/'),
        ),
    ]