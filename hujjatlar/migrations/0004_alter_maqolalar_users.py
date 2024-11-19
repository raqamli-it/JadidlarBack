# Generated by Django 5.0.1 on 2024-04-15 12:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hujjatlar', '0003_alter_maqolalar_create_alter_maqolalar_file_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='maqolalar',
            name='users',
            field=models.ManyToManyField(related_name='liked_maqolalar', to=settings.AUTH_USER_MODEL),
        ),
    ]