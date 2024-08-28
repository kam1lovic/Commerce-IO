from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    CheckConstraint,
    DecimalField,
    F,
    ForeignKey,
    IntegerField,
    Model,
    PositiveIntegerField,
    Q,
    TextChoices,
    TextField,
    URLField,
)

from shared.django.models import CreatedBaseModel


class Product(Model):  # ✅
    class StockStatus(TextChoices):
        FIXED = 'fixed', 'Fixed'
        INDEFINITE = 'indefinite', 'Indefinite'
        NOT_AVAILABLE = 'not_available', 'Not available'

    class Unit(TextChoices):
        ITEM = 'item', 'Item'
        WEIGHT = 'weight', 'Weight'

    name = CharField('Mahsulot nomi', max_length=100)
    category = ForeignKey('shops.Category', CASCADE, related_name='products')
    price = DecimalField('Sotuv narxi', max_digits=15, decimal_places=2)
    full_price = DecimalField('Umumiy narxi', max_digits=15, decimal_places=2, null=True, blank=True)
    description = TextField()
    has_available = BooleanField('Mahsulotni o`chirish va yoqish', default=True)
    weight = IntegerField('Vazni', null=True, blank=True)
    length = IntegerField("Uzunligi", null=True, blank=True)
    height = IntegerField('Balandligi', null=True, blank=True)
    width = IntegerField("Kengligi", null=True, blank=True)

    ikpu_code = IntegerField('IKPU ko`di', null=True, blank=True)
    package_code = IntegerField('qadoq ko`di', null=True, blank=True)
    stock_status = CharField(max_length=100, choices=StockStatus.choices)
    quantity = IntegerField('mahsulot soni status indefinite bo`lganda chiqadi', null=True, blank=True)
    barcode = IntegerField('Barkod', null=True, blank=True)
    vat_percent = IntegerField('QQS foizi', null=True, blank=True)
    position = IntegerField('sort order', db_default=1)
    internal_notes = TextField(null=True, blank=True)
    unit = CharField(max_length=20, choices=Unit.choices)
    weight_class = ForeignKey('shops.Weight', CASCADE, related_name='weights', null=True, blank=True)
    length_class = ForeignKey('shops.Length', CASCADE, related_name='lengths', null=True, blank=True)
    attachments = GenericRelation('shops.Attachment', object_id_field='record_id', blank=True)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(full_price__gte=F('price')), name='check_full_price')
        ]


class Attachment(CreatedBaseModel):
    content_type = ForeignKey('contenttypes.ContentType', CASCADE, null=True, blank=True, related_name='attachments')
    record_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'record_id')
    key = CharField(max_length=255, null=True, blank=True)
    url = URLField(null=True, blank=True)


class Attribute(Model):  # ✅
    name = CharField(max_length=50)
    product = ForeignKey('shops.Product', CASCADE, related_name='attributes')


class AttributeValue(Model):  # ✅
    value = CharField(max_length=20)
    attribute = ForeignKey('shops.Attribute', CASCADE, related_name='values')


class AttributeVariant(Model):  # ✅
    name = CharField(max_length=100)
    price = DecimalField('Sotuv narxi', max_digits=15, decimal_places=2)
    full_price = DecimalField('Umumiy narxi', max_digits=15, decimal_places=2)
    weight_class = ForeignKey('shops.Weight', CASCADE, null=True, blank=True, related_name='attribute_weights')
    length_class_id = ForeignKey('shops.Length', CASCADE, null=True, blank=True, related_name='attribute_lengths')
    weight = IntegerField('Vazni', null=True, blank=True)
    length = IntegerField('Uzunligi', null=True, blank=True)
    height = IntegerField('Balandligi', null=True, blank=True)
    width = IntegerField("Kengligi", null=True, blank=True)
    package_code = IntegerField('', null=True, blank=True)
    ikpu_code = IntegerField('IKPU kodi', null=True, blank=True)
    stock_status = CharField('Miqdorlar statusi', max_length=20)
    quantity = IntegerField('Miqdori', null=True, blank=True)
    unit = CharField('Qadoq kodi', max_length=20)
    barcode = IntegerField('Shtrix-kod', null=True, blank=True)
    has_available = BooleanField('Mavjud yoki mavjudmasligi', db_default=True)
    vat_percent = IntegerField('QQS foizi', db_default=0)
    product = ForeignKey('shops.Product', CASCADE, related_name='variants')
