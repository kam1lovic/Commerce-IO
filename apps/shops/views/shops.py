from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from shared.restframework.permissions import IsOwner
from shops.models import Shop
from shops.serializers.shops import ShopDynamicFieldsModelSerializer


@extend_schema(tags=['Shops'])
@extend_schema_view(
    list=extend_schema(
        responses=ShopDynamicFieldsModelSerializer(ref_name='shop_list', fields=['id', 'name', "status"])),
    create=extend_schema(responses=ShopDynamicFieldsModelSerializer(ref_name='shop_create',
                                                                    fields=["name", "category", "country",
                                                                            "phone_number",
                                                                            "currency", "languages", "owner", "phone",
                                                                            "status"])))
class ShopListCreateAPIView(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDynamicFieldsModelSerializer

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())

        if self.request.method == 'GET':
            return self.serializer_class(*args, ref_name='shop_list', **kwargs, fields=['name', 'category', 'status'])
        return self.serializer_class(*args, ref_name='shop_create', **kwargs,
                                     fields=['name', 'category', 'country', 'currency', 'phone', 'owner', 'status', 'phone_number'])


@extend_schema(tags=['Shops'])
class ShopRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    permission_classes = IsOwner, IsAuthenticated
    serializer_class = ShopDynamicFieldsModelSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())

        if self.request.method == 'PUT':
            return self.serializer_class(*args, **kwargs, exclude=['plan'])
