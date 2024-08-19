# Generated by Django 5.0.7 on 2024-08-14 04:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0002_initial'),
        ('shops', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shop',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='users.plan'),
        ),
        migrations.AddField(
            model_name='shop',
            name='services',
            field=models.ManyToManyField(through='orders.ShopService', to='orders.service'),
        ),
        migrations.AddField(
            model_name='commerce',
            name='shop',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sites', to='shops.shop'),
        ),
        migrations.AddField(
            model_name='category',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shops.shop'),
        ),
        migrations.AddField(
            model_name='broadcastmessage',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop'),
        ),
        migrations.AddField(
            model_name='shop',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shopcategory', verbose_name='Kategoriyalar'),
        ),
        migrations.AddField(
            model_name='telegrambot',
            name='shop',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='telegram_bots', to='shops.shop'),
        ),
        migrations.AddField(
            model_name='telegramchannel',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels', to='shops.shop'),
        ),
        migrations.AddField(
            model_name='channelmessage',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='shops.telegramchannel'),
        ),
        migrations.AddField(
            model_name='commerce',
            name='template_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', to='shops.templatecolor'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weights', to='shops.weight'),
        ),
        migrations.AddField(
            model_name='attributevariant',
            name='weight_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attribute_weights', to='shops.weight'),
        ),
        migrations.AlterUniqueTogether(
            name='telegramchannel',
            unique_together={('shop', 'chat')},
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.CheckConstraint(check=models.Q(('full_price__gte', models.F('price'))), name='check_full_price'),
        ),
    ]
