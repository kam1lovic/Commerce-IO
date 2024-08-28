from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    ForeignKey,
    IntegerField,
    Model,
    TextChoices,
    TextField,
)

from shared.django.models import CreatedBaseModel


class ShopCategory(Model):
    name = CharField('Nomi', max_length=100)

    class Meta:
        verbose_name = 'Do\'kon toifasi'
        verbose_name_plural = 'Do\'kon toifalari'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Category(CreatedBaseModel):  # ✅
    class Status(TextChoices):
        ACTIVE = 'active', 'Active'
        INACTIVE = 'inactive', 'Inactive'

    name = CharField('Nomi', max_length=255)
    emoji = CharField('Emoji', max_length=25, null=True, blank=True)
    parent = ForeignKey('self', CASCADE, blank=True, null=True, related_name='children')
    show_in_ecommerce = BooleanField("Web saytda ko'rsatish", db_default=False)
    status = CharField('Holati', max_length=15, choices=Status.choices, db_default=Status.INACTIVE)
    description = TextField('Tavsif', null=True, blank=True)
    position = IntegerField(default=1)
    shop = ForeignKey('shops.Shop', CASCADE, related_name='categories')
    attachments = GenericRelation('shops.Attachment', blank=True, object_id_field='record_id')

    class Meta:
        ordering = ('name',)
