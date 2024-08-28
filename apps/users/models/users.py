from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models import (
    CASCADE,
    SET_NULL,
    BigIntegerField,
    BooleanField,
    CharField,
    DateTimeField,
    EmailField,
    ForeignKey,
    Model,
    OneToOneField,
    TextChoices,
)

from shared.django.managers import CustomUserManager


class Person(Model):  # ✅
    name = CharField(max_length=255)
    phone = CharField(max_length=25)


class ShopUser(AbstractBaseUser):  # ✅
    class Type(TextChoices):
        EMAIL = 'email', 'Email'
        TELEGRAM = 'telegram', 'Telegram'
        FACEBOOK = 'facebook', 'Facebook'

    username = CharField(max_length=150, unique=True, validators=[UnicodeUsernameValidator()])

    last_activity = DateTimeField(auto_now_add=True)
    is_blocked = BooleanField(db_default=False)
    telegram_id = BigIntegerField(blank=True, null=True, unique=True)
    person = OneToOneField('users.Person', SET_NULL, null=True, blank=True)

    type = CharField(max_length=25)
    first_name = CharField(max_length=150, blank=True)
    last_name = CharField(max_length=150, blank=True)
    email = EmailField(blank=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=False)

    language = ForeignKey('shops.Language', CASCADE)
    shop = ForeignKey('shops.Shop', CASCADE, related_name='customers')
    created_at = DateTimeField(auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        unique_together = [
            ('username', 'shop')
        ]


class User(AbstractBaseUser, PermissionsMixin):  # ✅
    class Type(TextChoices):
        EMAIL = 'email', 'Email'
        TELEGRAM = 'telegram', 'Telegram'
        FACEBOOK = 'facebook', 'Facebook'

    type = CharField(max_length=25)
    username = CharField('Foydalanuvchi nomi', max_length=150, null=True, blank=True, unique=True,
                         validators=[UnicodeUsernameValidator()])
    first_name = CharField('Ism', max_length=150, blank=True)
    last_name = CharField('Familiya', max_length=150, blank=True)
    email = EmailField('Email', unique=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=False)

    language = ForeignKey('shops.Language', CASCADE, null=True, blank=True)
    public_offer = BooleanField('Ommaviy taklif', default=False)
    invitation_code = CharField('Taflifnoma kodi', max_length=25, unique=True, null=True)
    created_at = DateTimeField(auto_now=True)
    default_shop = OneToOneField('shops.Shop', SET_NULL, blank=True, null=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
