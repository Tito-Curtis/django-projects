# Generated by Django 5.0.1 on 2024-03-11 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_category_productimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='meetings',
            options={'verbose_name_plural': 'Meetings'},
        ),
    ]
