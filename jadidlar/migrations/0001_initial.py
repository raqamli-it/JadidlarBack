# Generated by Django 5.0.1 on 2024-02-21 07:32

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jadid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('fullname_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('fullname_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('fullname_en', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('die_day', models.DateField(blank=True, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='image/jadid')),
                ('order', models.IntegerField(default=1000)),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('bio_ru', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('bio_uz', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('bio_en', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Jadid',
                'verbose_name_plural': 'Jadidlar',
            },
        ),
        migrations.CreateModel(
            name='JadidImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('jadid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jadid_images', to='jadidlar.jadid')),
            ],
        ),
    ]
