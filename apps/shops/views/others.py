from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from shops.models import Country
from shops.serializers.others import CountryModelSerializer


@extend_schema(tags=['Others'])
class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer
