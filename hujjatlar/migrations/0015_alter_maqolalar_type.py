# Generated by Django 5.0.1 on 2024-04-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hujjatlar', '0014_alter_arxiv_hujjatlar_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maqolalar',
            name='type',
            field=models.CharField(blank=True, choices=[('Tarix', 'Tarix'), ('Siyosat', 'Siyosat'), ('Iqtisod', 'Iqtisod'), ('Madaniyat_va_sanat', 'Madaniyat_va_sanat'), ('Ijtimoiy_masalalar_va_din', 'Ijtimoiy_masalalar_va_din'), ('Adabiyot', 'Adabiyot'), ('Talim_Tarbiya', 'Talim_Tarbiya'), ('Boshqa_masalalar', 'Boshqa_masalalar'), ('Bibliografik_korsatkich', 'Bibliografik_korsatkich')], max_length=30, null=True, verbose_name='matbuotlar'),
        ),
    ]
