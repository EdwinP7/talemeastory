# Generated by Django 2.2.17 on 2021-02-16 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talegate', '0003_auto_20210129_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excerpt',
            name='text',
            field=models.TextField(max_length=255),
        ),
    ]
