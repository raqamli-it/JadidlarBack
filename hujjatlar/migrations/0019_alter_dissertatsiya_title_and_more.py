# Generated by Django 5.0.1 on 2024-07-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hujjatlar', '0018_alter_asarlar_title_alter_asarlar_title_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dissertatsiya',
            name='title',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='dissertatsiya',
            name='title_en',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='dissertatsiya',
            name='title_ru',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='dissertatsiya',
            name='title_uz',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='hotiralar',
            name='title',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='hotiralar',
            name='title_en',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='hotiralar',
            name='title_ru',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='hotiralar',
            name='title_uz',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='sherlar',
            name='title',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='sherlar',
            name='title_en',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='sherlar',
            name='title_ru',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='sherlar',
            name='title_uz',
            field=models.TextField(blank=True, null=True, verbose_name='nomi'),
        ),
    ]