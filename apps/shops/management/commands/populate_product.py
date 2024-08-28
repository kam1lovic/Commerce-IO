import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from faker import Faker
from shops.models import Category, Length, Product, Weight


class Command(BaseCommand):
    help = 'Populates the Product model with fake data'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=int, help='Number of fake records to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        fake = Faker()

        # Fetch existing categories, weights, and lengths to assign to the products
        categories = list(Category.objects.all())
        weights = list(Weight.objects.all())
        lengths = list(Length.objects.all())

        if not categories:
            self.stdout.write(self.style.ERROR('No categories found in the database. Please add some first.'))
            return

        for _ in range(count):
            price = Decimal(fake.pydecimal(left_digits=4, right_digits=2, positive=True))
            full_price = Decimal(fake.pydecimal(left_digits=4, right_digits=2, positive=True))

            if full_price < price:
                full_price = price + Decimal('1.00')

            Product.objects.create(
                name=fake.word(),
                category=random.choice(categories),
                price=price,
                full_price=full_price,
                description=fake.text(max_nb_chars=200),
                has_available=fake.boolean(),
                stock_status=random.choice(
                    [Product.StockStatus.FIXED, Product.StockStatus.INDEFINITE, Product.StockStatus.NOT_AVAILABLE]),
                quantity=random.randint(0, 1000) if random.choice([True, False]) else 0,
                vat_percent=random.choice([0, 5, 10, 20]),
                position=fake.random_int(min=1, max=100),
                internal_notes=fake.text(max_nb_chars=100) if random.choice([True, False]) else None,
                unit=random.choice([Product.Unit.ITEM, Product.Unit.WEIGHT]),
                weight_class=random.choice(weights) if weights else None,
                length_class=random.choice(lengths) if lengths else None
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully populated the Product model with {count} fake records'))
