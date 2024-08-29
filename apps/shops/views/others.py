from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from shops.models import Country, Currency
from shops.serializers.others import CountryModelSerializer


@extend_schema(tags=['Others'])
class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer


@extend_schema(tags=['Others'])
class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CountryModelSerializer
