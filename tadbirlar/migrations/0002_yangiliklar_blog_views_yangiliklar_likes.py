# Generated by Django 5.0.1 on 2024-02-26 14:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tadbirlar', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='yangiliklar',
            name='blog_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='yangiliklar',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_jadids', to=settings.AUTH_USER_MODEL),
        ),
    ]
