# Generated by Django 5.0.7 on 2024-08-29 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='shopcategory',
            options={'ordering': ('name',), 'verbose_name': "Do'kon toifasi", 'verbose_name_plural': "Do'kon toifalari"},
        ),
    ]
