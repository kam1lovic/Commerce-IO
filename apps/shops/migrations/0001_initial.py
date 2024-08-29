# Generated by Django 5.0.7 on 2024-08-22 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BroadCastMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=4100, verbose_name='Xabar')),
                ('is_scheduled', models.BooleanField(default=False)),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Lokatsiya lat')),
                ('lon', models.FloatField(blank=True, null=True, verbose_name='Lokatsiya lon')),
                ('scheduled_time', models.DateTimeField(blank=True, null=True, verbose_name="Keyinroq jo'natish vaqti")),
                ('received_users', models.IntegerField(default=0, verbose_name='Qabul qiluvchilar soni')),
                ('status', models.CharField(choices=[('sent', 'Sent'), ('pending', 'Pending'), ('not_sent', 'Not sent')], db_default='pending', max_length=20, verbose_name='Xabarning statusi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
            ],
            options={
                'verbose_name': 'Axborotnoma',
                'verbose_name_plural': 'Axborotnomalar',
            },
        ),
        migrations.CreateModel(
            name='ChannelMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=4100)),
                ('is_scheduled', models.BooleanField(default=False, verbose_name="Keyinroq jo'natilsinmi?")),
                ('scheduled_time', models.DateTimeField(blank=True, null=True, verbose_name="Keyinroq jo'natish vaqti")),
                ('file_type', models.CharField(choices=[('text', 'Text'), ('photo', 'Photo'), ('video', 'Video')], db_default='text', max_length=20)),
                ('status', models.CharField(choices=[('sent', 'Sent'), ('pending', 'Pending'), ('not_sent', 'Not sent')], db_default='pending', max_length=20, verbose_name='Xabarning statusi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Xabar yaratilgan vaqti')),
            ],
            options={
                'verbose_name': 'Telegram kanal xabari',
                'verbose_name_plural': 'Telegram kanal xabarlari',
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=4100, verbose_name='Xabar')),
                ('content_type', models.CharField(choices=[('user', 'User'), ('owner', 'Owner')], max_length=10)),
                ('seen', models.BooleanField(db_default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
            ],
        ),
        migrations.CreateModel(
            name='Commerce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Domen Nomi')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=8, verbose_name='Sayt aktiv yoki  aktivmasligi')),
                ('is_configured', models.BooleanField(db_default=True)),
                ('is_sub_domain', models.BooleanField(db_default=True, verbose_name='Sayt domen qo`ygan yoki qo`ymaganligi')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Davlat',
                'verbose_name_plural': 'Davlatlar',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('order', models.PositiveSmallIntegerField(db_default=1, default=1, verbose_name='Rangi')),
            ],
            options={
                'verbose_name': 'Pul birligi',
                'verbose_name_plural': 'Pul birliklari',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Nomi')),
                ('code', models.CharField(max_length=10, verbose_name='Kodi')),
                ('icon', models.CharField(max_length=10, verbose_name='Belgisi')),
            ],
        ),
        migrations.CreateModel(
            name='Length',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': "Do'kon toifasi",
                'verbose_name_plural': "Do'kon toifalari",
            },
        ),
        migrations.CreateModel(
            name='TelegramBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Telegram username')),
                ('token', models.CharField(max_length=255, unique=True, verbose_name='BotFather dan olingan token')),
                ('group_access_token', models.CharField(max_length=255, unique=True, verbose_name='guruhda ishlashi uchun token')),
                ('is_new_template', models.BooleanField(verbose_name='web app True oddiy bot False')),
                ('order_button_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TelegramChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=255, verbose_name='Telegram kanal username')),
            ],
            options={
                'verbose_name': 'Telegram kanal',
                'verbose_name_plural': 'Telegram kanallar',
            },
        ),
        migrations.CreateModel(
            name='TemplateColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Nomi')),
                ('color', models.CharField(max_length=55, verbose_name='Rangi')),
            ],
            options={
                'verbose_name': 'Shablon rangi',
                'verbose_name_plural': 'Shablon ranglari',
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('record_id', models.PositiveIntegerField()),
                ('key', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='shops.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('emoji', models.CharField(blank=True, max_length=25, null=True, verbose_name='Emoji')),
                ('show_in_ecommerce', models.BooleanField(db_default=False, verbose_name="Web saytda ko'rsatish")),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], db_default='inactive', max_length=15, verbose_name='Holati')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Tavsif')),
                ('position', models.IntegerField(default=1)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shops.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Mahsulot nomi')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Sotuv narxi')),
                ('full_price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Umumiy narxi')),
                ('description', models.TextField()),
                ('has_available', models.BooleanField(default=True, verbose_name='Mahsulotni o`chirish va yoqish')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='Vazni')),
                ('length', models.IntegerField(blank=True, null=True, verbose_name='Uzunligi')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='Balandligi')),
                ('width', models.IntegerField(blank=True, null=True, verbose_name='Kengligi')),
                ('ikpu_code', models.IntegerField(blank=True, null=True, verbose_name='IKPU ko`di')),
                ('package_code', models.IntegerField(blank=True, null=True, verbose_name='qadoq ko`di')),
                ('stock_status', models.CharField(choices=[('fixed', 'Fixed'), ('indefinite', 'Indefinite'), ('not_available', 'Not available')], max_length=100)),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='mahsulot soni status indefinite bo`lganda chiqadi')),
                ('barcode', models.IntegerField(blank=True, null=True, verbose_name='Barkod')),
                ('vat_percent', models.IntegerField(blank=True, null=True, verbose_name='QQS foizi')),
                ('position', models.IntegerField(db_default=1, verbose_name='sort order')),
                ('internal_notes', models.TextField(blank=True, null=True)),
                ('unit', models.CharField(choices=[('item', 'Item'), ('weight', 'Weight')], max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shops.category')),
                ('length_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lengths', to='shops.length')),
            ],
        ),
        migrations.CreateModel(
            name='AttributeVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Sotuv narxi')),
                ('full_price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Umumiy narxi')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='Vazni')),
                ('length', models.IntegerField(blank=True, null=True, verbose_name='Uzunligi')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='Balandligi')),
                ('width', models.IntegerField(blank=True, null=True, verbose_name='Kengligi')),
                ('package_code', models.IntegerField(blank=True, null=True, verbose_name='')),
                ('ikpu_code', models.IntegerField(blank=True, null=True, verbose_name='IKPU kodi')),
                ('stock_status', models.CharField(max_length=20, verbose_name='Miqdorlar statusi')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Miqdori')),
                ('unit', models.CharField(max_length=20, verbose_name='Qadoq kodi')),
                ('barcode', models.IntegerField(blank=True, null=True, verbose_name='Shtrix-kod')),
                ('has_available', models.BooleanField(db_default=True, verbose_name='Mavjud yoki mavjudmasligi')),
                ('vat_percent', models.IntegerField(db_default=0, verbose_name='QQS foizi')),
                ('length_class_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attribute_lengths', to='shops.length')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='shops.product')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='shops.product'),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name="Do'kon nomi")),
                ('phone', models.CharField(max_length=50, verbose_name='Biznes telefon raqami')),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefon raqami')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], db_default='active', max_length=8)),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Location lat')),
                ('lon', models.FloatField(blank=True, null=True, verbose_name='Location lon')),
                ('starts_at', models.TimeField(blank=True, null=True, verbose_name='Dan')),
                ('ends_at', models.TimeField(blank=True, null=True, verbose_name='Gacha')),
                ('has_terminal', models.BooleanField(db_default=True)),
                ('about_us', models.TextField(blank=True, null=True, verbose_name='Biz haqimizda')),
                ('facebook', models.URLField(blank=True, max_length=255, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, max_length=255, null=True, verbose_name='Instagram')),
                ('telegram', models.URLField(blank=True, max_length=255, null=True, verbose_name='Telegram')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Elektron pochta')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Manzil')),
                ('is_new_products_show', models.BooleanField(db_default=False, default=False, verbose_name="'Yangi mahsulotlar' sahifasini ko'rsatish")),
                ('is_popular_products_show', models.BooleanField(db_default=False, default=False, verbose_name="'Ommabop mahsulotlar' sahifasini ko'rsatish")),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.country', verbose_name="Ro'yxatdan o'tgan davlat")),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.currency', verbose_name='Pul birligi')),
                ('languages', models.ManyToManyField(blank=True, to='shops.language', verbose_name='Til')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
