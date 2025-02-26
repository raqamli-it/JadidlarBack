# Generated by Django 5.0.1 on 2024-04-15 11:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hujjatlar', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='maqolalar',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='maqolalar',
            name='turkiston_muxtoriyati',
            field=models.BooleanField(default=False, verbose_name='Turkiston muxtoriyati'),
        ),
        migrations.AlterField(
            model_name='maqolalar',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_maqolalar', to=settings.AUTH_USER_MODEL),
        ),
    ]
