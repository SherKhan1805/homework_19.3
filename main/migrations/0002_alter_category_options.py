# Generated by Django 4.2.7 on 2023-11-19 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
    ]
