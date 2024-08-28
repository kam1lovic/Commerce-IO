from django.db.models import (
    CASCADE,
    RESTRICT,
    CharField,
    DateField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    Model,
    PositiveIntegerField,
    TextChoices,
    TextField,
    URLField,
)
from shared.django.models import CreatedBaseModel


class Plan(CreatedBaseModel):  # ✅
    name = CharField('Nomi', max_length=150)
    code = CharField('Kod', max_length=150)
    description = TextField('Tavsif', max_length=150)
    quotas = ManyToManyField('users.Quotas', through='users.PlanQuotas', blank=True)


class PlanPricing(CreatedBaseModel):  # ✅
    class PeriodType(TextChoices):
        MONTHLY = 'monthly', 'Monthly'
        ANNUAL = 'annual', 'Annual'

    name = CharField('Nomi', max_length=50)
    period_type = CharField('Davr turi', max_length=25, choices=PeriodType.choices, db_default=PeriodType.MONTHLY)
    currency = ForeignKey('shops.Currency', RESTRICT)

    price = PositiveIntegerField('Narxi')
    original_price = PositiveIntegerField('Haqiqiy narxi')
    period = IntegerField('Davr')
    plan = ForeignKey('users.Plan', CASCADE)


class Quotas(CreatedBaseModel):  # ✅
    name = CharField('Nomi', max_length=150)
    description = TextField('Tavsif', blank=True)


class PlanQuotas(Model):
    plan = ForeignKey('users.Plan', CASCADE)
    quotas = ForeignKey('users.Quotas', CASCADE)
    value = CharField('Qiymat', max_length=50)


class PlanInvoice(CreatedBaseModel):  # ✅
    class Status(TextChoices):
        NEW = 'new', 'New'
        COMPLETED = 'completed', 'Completed'

    price = CharField('Narxi', max_length=55)
    user = ForeignKey('users.User', CASCADE, related_name='plan_invoices')
    plan = ForeignKey('users.Plan', CASCADE)
    payed_at = DateTimeField('da toʻlangan', null=True, blank=True)
    pay_url = URLField('tolov url', null=True, blank=True)
    plan_extended_from = DateField()
    plan_extended_until = DateField(null=True, blank=True)
    status = CharField(max_length=25, choices=Status.choices, db_default=Status.NEW)
