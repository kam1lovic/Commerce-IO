from factory.django import DjangoModelFactory

from shops.models import Category


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category
