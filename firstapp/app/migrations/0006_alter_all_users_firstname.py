# Generated by Django 5.0.1 on 2024-03-16 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_all_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_users',
            name='firstName',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
