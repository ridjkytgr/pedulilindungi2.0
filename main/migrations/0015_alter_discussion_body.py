# Generated by Django 3.2.8 on 2021-10-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_discussion_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='body',
            field=models.TextField(max_length=1000),
        ),
    ]
