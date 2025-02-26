# Generated by Django 5.0.1 on 2024-03-06 07:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manbalar', '0003_audiolar_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rasmlar',
            name='blog_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rasmlar',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_rasmlar', to=settings.AUTH_USER_MODEL),
        ),
    ]
