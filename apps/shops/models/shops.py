from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    EmailField,
    FloatField,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    Model,
    OneToOneField,
    TextChoices,
    TextField,
    TimeField,
    URLField,
)

from shared.django.models import CreatedBaseModel


class Shop(CreatedBaseModel):
    class Status(TextChoices):
        ACTIVE = 'active', 'Active'
        IN_ACTIVE = 'inactive', 'Inactive'

    name = CharField("Do'kon nomi", max_length=255)
    phone = CharField("Biznes telefon raqami", max_length=50)
    phone_number = CharField("Telefon raqami", max_length=50, null=True, blank=True)

    country = ForeignKey("shops.Country", CASCADE, verbose_name="Ro'yxatdan o'tgan davlat")
    languages = ManyToManyField("shops.Language", blank=True, verbose_name="Til")
    services = ManyToManyField('orders.Service', through='orders.ShopService')
    category = ForeignKey("shops.ShopCategory", CASCADE, verbose_name="Kategoriyalar")
    status = CharField(max_length=8, choices=Status.choices, db_default=Status.ACTIVE)
    currency = ForeignKey("shops.Currency", CASCADE, verbose_name="Pul birligi")
    plan = ForeignKey('users.Plan', CASCADE, related_name='shops')
    owner = ForeignKey('users.User', CASCADE, related_name='shops')
    lat = FloatField('Location lat', blank=True, null=True)
    lon = FloatField('Location lon', blank=True, null=True)
    starts_at = TimeField('Dan', blank=True, null=True)
    ends_at = TimeField('Gacha', blank=True, null=True)
    has_terminal = BooleanField(db_default=True)
    about_us = TextField("Biz haqimizda", null=True, blank=True)
    facebook = URLField("Facebook", max_length=255, null=True, blank=True)
    instagram = URLField("Instagram", max_length=255, null=True, blank=True)
    telegram = URLField('Telegram', max_length=255, null=True, blank=True)
    email = EmailField("Elektron pochta", max_length=255, null=True, blank=True)
    address = CharField('Manzil', max_length=500, null=True, blank=True)
    is_new_products_show = BooleanField("'Yangi mahsulotlar' sahifasini ko'rsatish", default=False, db_default=False)
    is_popular_products_show = BooleanField("'Ommabop mahsulotlar' sahifasini ko'rsatish", default=False,
                                            db_default=False)
    attachments = GenericRelation('shops.Attachment', blank=True, object_id_field='record_id')
    shop_logo = GenericRelation('shops.Attachment', blank=True, object_id_field='record_id')
    favicon_image = GenericRelation('shops.Attachment', blank=True, object_id_field='record_id')
    slider_images = GenericRelation('shops.Attachment', blank=True, object_id_field='record_id')


class TelegramChannel(Model):  # ✅
    chat = CharField('Telegram kanal username', max_length=255)
    shop = ForeignKey('shops.Shop', CASCADE, related_name='channels')

    class Meta:
        verbose_name = 'Telegram kanal'
        verbose_name_plural = 'Telegram kanallar'
        unique_together = [
            ('shop', 'chat')
        ]

    def __str__(self):
        return f"{self.chat}"


class ChannelMessage(Model):  # ✅
    class FileType(TextChoices):
        TEXT = 'text', 'Text'
        PHOTO = 'photo', 'Photo'
        VIDEO = 'video', 'Video'

    class MessageStatus(TextChoices):
        SENT = 'sent', 'Sent'
        PENDING = 'pending', 'Pending'
        NOT_SENT = 'not_sent', 'Not sent'

    message = CharField(max_length=4100)
    chat = ForeignKey('shops.TelegramChannel', CASCADE, related_name='messages')
    is_scheduled = BooleanField("Keyinroq jo'natilsinmi?", default=False)
    scheduled_time = DateTimeField("Keyinroq jo'natish vaqti", blank=True, null=True)
    file_type = CharField(max_length=20, choices=FileType.choices, db_default=FileType.TEXT)
    status = CharField('Xabarning statusi', max_length=20, choices=MessageStatus.choices,
                       db_default=MessageStatus.PENDING)
    created_at = DateTimeField('Xabar yaratilgan vaqti', auto_now_add=True)

    class Meta:
        verbose_name = 'Telegram kanal xabari'
        verbose_name_plural = 'Telegram kanal xabarlari'

    def __str__(self):
        return f"{self.id}. Message of {self.chat}"


class ChatMessage(Model):  # ✅
    class Type(TextChoices):
        USER = 'user', 'User'
        OWNER = 'owner', 'Owner'

    class ContentType(TextChoices):
        TEXT = 'text', 'Text'

    message = CharField('Xabar', max_length=4100)
    content_type = CharField(max_length=10, choices=Type.choices)
    seen = BooleanField(db_default=False)
    created_at = DateTimeField('Yaratilgan vaqti', auto_now_add=True)


class BroadCastMessage(Model):  # ✅
    class MessageStatus(TextChoices):
        SENT = 'sent', 'Sent'
        PENDING = 'pending', 'Pending'
        NOT_SENT = 'not_sent', 'Not sent'

    message = CharField('Xabar', max_length=4100)
    shop = ForeignKey('shops.Shop', CASCADE)
    is_scheduled = BooleanField(default=False)
    lat = FloatField("Lokatsiya lat", blank=True, null=True)
    lon = FloatField("Lokatsiya lon", blank=True, null=True)
    scheduled_time = DateTimeField("Keyinroq jo'natish vaqti", blank=True, null=True)
    received_users = IntegerField('Qabul qiluvchilar soni', default=0)
    status = CharField('Xabarning statusi', max_length=20, choices=MessageStatus.choices,
                       db_default=MessageStatus.PENDING)
    attachments = GenericRelation('shops.Attachment', blank=True, object_id_field='record_id')
    created_at = DateTimeField('Yaratilgan sana', auto_now_add=True)

    class Meta:
        verbose_name = 'Axborotnoma'
        verbose_name_plural = 'Axborotnomalar'


class Commerce(Model):  # ✅
    class Status(TextChoices):
        ACTIVE = 'active', 'Active'
        INACTIVE = 'inactive', 'Inactive'

    name = CharField('Domen Nomi', max_length=30)
    status = CharField('Sayt aktiv yoki  aktivmasligi', max_length=8, choices=Status.choices)
    template_color = ForeignKey('shops.TemplateColor', CASCADE, related_name='sites')
    is_configured = BooleanField(db_default=True)
    is_sub_domain = BooleanField('Sayt domen qo`ygan yoki qo`ymaganligi', db_default=True)
    shop = OneToOneField('shops.Shop', CASCADE, related_name='sites')


class TelegramBot(Model):  # ✅
    username = CharField("Telegram username", max_length=255, unique=True)
    token = CharField('BotFather dan olingan token', max_length=255, unique=True)
    group_access_token = CharField('guruhda ishlashi uchun token', max_length=255, unique=True)
    is_new_template = BooleanField('web app True oddiy bot False')
    order_button_url = CharField(max_length=255)
    shop = OneToOneField('shops.Shop', CASCADE, related_name='telegram_bots')
