# Generated by Django 5.0.1 on 2024-02-26 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jadidlar', '0002_jadid_blog_views_jadid_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jadid',
            name='blog_views',
        ),
        migrations.RemoveField(
            model_name='jadid',
            name='likes',
        ),
    ]
