# Generated by Django 3.2.7 on 2021-11-03 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('role', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
    ]