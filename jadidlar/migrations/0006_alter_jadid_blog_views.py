# Generated by Django 5.0.1 on 2024-03-06 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jadidlar', '0005_remove_jadid_likes_alter_jadid_blog_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadid',
            name='blog_views',
            field=models.IntegerField(default=0),
        ),
    ]
