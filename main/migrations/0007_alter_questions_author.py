# Generated by Django 3.2.8 on 2021-10-26 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20211025_2150'),
        ('main', '0006_alter_questions_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
    ]
