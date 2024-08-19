import random

from django.core.management.base import BaseCommand
from faker import Faker
from shops.models import Language
from users.models import User


class Command(BaseCommand):
    help = 'Foydalanuvchilar jadvalini soxta malumotlar bilan to\'ldirish'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):

        languages = list(Language.objects.all())

        if not languages:
            self.stdout.write(self.style.ERROR('No languages found'))
            return

        count = kwargs['count']
        fake = Faker()
        for _ in range(count):
            User.objects.create(
                first_name=fake.name(),
                last_name=fake.name(),
                email=fake.email(),
                is_active=True,
                is_staff=True,
                is_superuser=True,
                public_offer=False,
                language_id=random.choice(languages).id
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully populated the database with {count} fake records'))
