# Generated by Django 5.1 on 2024-08-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_model',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
