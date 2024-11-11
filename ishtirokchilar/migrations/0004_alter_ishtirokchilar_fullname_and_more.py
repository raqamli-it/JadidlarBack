# Generated by Django 5.0.1 on 2024-04-19 06:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ishtirokchilar', '0003_alter_ishtirokchilar_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ishtirokchilar',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_fullname', message='Bu maydon "#"-belgisini o\'z ichiga olmaydi.', regex='^[^#]+$')]),
        ),
        migrations.AlterField(
            model_name='ishtirokchilar',
            name='fullname_en',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_fullname', message='Bu maydon "#"-belgisini o\'z ichiga olmaydi.', regex='^[^#]+$')]),
        ),
        migrations.AlterField(
            model_name='ishtirokchilar',
            name='fullname_ru',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_fullname', message='Bu maydon "#"-belgisini o\'z ichiga olmaydi.', regex='^[^#]+$')]),
        ),
        migrations.AlterField(
            model_name='ishtirokchilar',
            name='fullname_uz',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_fullname', message='Bu maydon "#"-belgisini o\'z ichiga olmaydi.', regex='^[^#]+$')]),
        ),
    ]
