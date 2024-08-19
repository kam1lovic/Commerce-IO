import random

from django.core.management import BaseCommand
from faker import Faker
from shops.models import Country, Currency, Shop, ShopCategory
from users.models import Plan, User


class Command(BaseCommand):
    help = 'Shop modelini soxta malumotlar bilan to\'ldirish'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        fake = Faker()

        countries = list(Country.objects.all())
        owner = list(User.objects.all())
        plan = list(Plan.objects.all())
        category = list(ShopCategory.objects.all())
        currency = list(Currency.objects.all())

        if not countries or not owner or not plan or not category or not currency:
            self.stdout.write(self.style.ERROR('Missing arguments'))
            return

        for _ in range(count):
            Shop.objects.create(
                name=fake.name(),
                phone=fake.phone_number(),
                country_id=random.choice(countries).id,
                owner_id=random.choice(owner).id,
                plan_id=random.choice(plan).id,
                currency_id=random.choice(currency).id,
                category_id=random.choice(category).id,

            )

        self.stdout.write(self.style.SUCCESS(f'Successfully populated the database with {count} fake records'))
