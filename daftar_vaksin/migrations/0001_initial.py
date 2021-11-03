# Generated by Django 3.2.7 on 2021-11-03 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('biodata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JadwalVaksin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kota', models.CharField(max_length=255)),
                ('tanggal', models.DateField()),
                ('jenis_vaksin', models.CharField(default='', max_length=255)),
                ('tempat', models.CharField(max_length=255)),
                ('penerima', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biodata.peserta')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biodata.penyedia')),
            ],
        ),
    ]
