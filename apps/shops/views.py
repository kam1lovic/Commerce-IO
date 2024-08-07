from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from shared.restframework.custom_permissions import IsOwnerShop
from shops.models import Shop, Country
from shops.serializers import ShopModelSerializer, CountryModelSerializer


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer


@extend_schema(tags=['Shops'])
class ShopListCreateAPIView(ListCreateAPIView):
    queryset = Shop.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ShopModelSerializer

    def get_queryset(self):
        return Shop.objects.filter(owner=self.request.user)

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())

        if self.request.method == 'POST':
            return self.serializer_class(*args, **kwargs,
                                         fields=['name', 'category', 'country', 'languages', 'currency', 'phone'])
        return self.serializer_class(*args, **kwargs, fields=['name', 'category'])


@extend_schema(tags=['Shops'])
class ShopRetrieveDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    permission_classes = IsAuthenticated, IsOwnerShop
    serializer_class = ShopModelSerializer
