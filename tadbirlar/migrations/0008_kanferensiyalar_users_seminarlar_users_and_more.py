# Generated by Django 5.0.1 on 2024-03-10 08:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tadbirlar', '0007_kanferensiyalar_blog_views_kanferensiyalar_likes_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='kanferensiyalar',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='liked_kanferensiyalar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='seminarlar',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='liked_seminarlar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='yangiliklar',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='liked_yangiliklar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='kanferensiyalar',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='seminarlar',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='yangiliklar',
            name='likes',
        ),
        migrations.AddField(
            model_name='kanferensiyalar',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seminarlar',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='yangiliklar',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
