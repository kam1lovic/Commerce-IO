from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from shared.restframework.permissions import IsOwnerShop
from shops.models import Shop
from shops.serializers.shops import ShopDynamicFieldsModelSerializer


@extend_schema(tags=['Shops'])
class ShopListCreateAPIView(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDynamicFieldsModelSerializer

    def get_queryset(self):
        return Shop.objects.filter(owner=self.request.user)

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())

        if self.request.method == 'GET':
            return self.serializer_class(*args, **kwargs, fields=['name', 'category', 'status'])
        return self.serializer_class(*args, **kwargs,
                                     fields=['name', 'category', 'country', 'currency', 'phone', 'owner'])


@extend_schema(tags=['Shops'])
class ShopRetrieveDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    permission_classes = IsOwnerShop,
    serializer_class = ShopDynamicFieldsModelSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())

        if self.request.method == 'PUT':
            return self.serializer_class(*args, **kwargs, exclude=['plan'])
