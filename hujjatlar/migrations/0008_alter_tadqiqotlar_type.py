# Generated by Django 5.0.1 on 2024-04-19 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hujjatlar', '0007_alter_sherlar_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tadqiqotlar',
            name='type',
            field=models.CharField(blank=True, choices=[('Turkiston_muxtoriyati', 'Turkiston_muxtoriyati'), ('Tadqiqotlar', 'Tadqiqotlar'), ('Til_va_imlo', 'Til_va_imlo')], default='Turkiston_muxtoriyati', max_length=25, null=True, verbose_name='turi'),
        ),
    ]
