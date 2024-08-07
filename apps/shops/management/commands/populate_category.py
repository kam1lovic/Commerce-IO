import random

from django.core.management.base import BaseCommand
from faker import Faker

from shops.models import Shop, Category


class Command(BaseCommand):
    help = 'Populates the Category model with fake data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of fake records to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        fake = Faker()

        # Fetch existing shops to assign to the categories
        shops = list(Shop.objects.all())

        if not shops:
            self.stdout.write(self.style.ERROR('No shops found in the database. Please add some first.'))
            return

        for _ in range(count):
            Category.objects.create(
                name=fake.word(),
                emoji=fake.random_element(elements=['🍎', '🍌', '🍓', '🍇', '🍉', '🍑', '🍍']),
                parent=random.choice(Category.objects.all() or [None]),
                show_in_ecommerce=fake.boolean(),
                status=random.choice([Category.Status.ACTIVE, Category.Status.INACTIVE]),
                description=fake.text(max_nb_chars=200),
                position=fake.random_int(min=1, max=100),
                shop=random.choice(shops)
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully populated the Category model with {count} fake records'))
