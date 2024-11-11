# Generated by Django 5.0.1 on 2024-02-21 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tanlovlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Telegram', 'Telegram'), ('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Email', 'Email'), ('Telefon', 'Telefon')], default='Telegram', max_length=50, verbose_name='turi')),
                ('qiymat', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Tanlov',
                'verbose_name_plural': 'Tanlovlar',
            },
        ),
    ]
