# Generated by Django 3.2.7 on 2021-10-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_vaksin', '0003_auto_20211028_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwalvaksin',
            name='jenis_vaksin',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='jadwalvaksin',
            name='kota',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='jadwalvaksin',
            name='tanggal',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='jadwalvaksin',
            name='waktu',
            field=models.CharField(default='', max_length=30),
        ),
    ]
