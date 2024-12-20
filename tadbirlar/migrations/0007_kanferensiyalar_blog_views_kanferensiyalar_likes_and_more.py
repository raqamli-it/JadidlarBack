# Generated by Django 5.0.1 on 2024-03-06 07:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tadbirlar', '0006_alter_yangiliklar_blog_views'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='kanferensiyalar',
            name='blog_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kanferensiyalar',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_kanferensiyalar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='seminarlar',
            name='blog_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seminarlar',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_seminarlar', to=settings.AUTH_USER_MODEL),
        ),
    ]
