from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, UpdateAPIView

from shared.restframework.paginations import CustomPagination
from shared.restframework.permissions import IsOwner
from shops.models.categories import Category
from shops.serializers.category import ShopCategoryDynamicFieldsModelSerializer


@extend_schema(tags=['Category'])
@extend_schema_view(
    list=extend_schema(
        responses=ShopCategoryDynamicFieldsModelSerializer(ref_name='category_list',
                                                           fields=['id', 'name'])),
    create=extend_schema(responses=ShopCategoryDynamicFieldsModelSerializer(ref_name='category_create',
                                                                            fields=['name', 'parent',
                                                                                    'description', 'position'])))
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = ShopCategoryDynamicFieldsModelSerializer
    pagination_class = CustomPagination
    filter_backends = (SearchFilter,)
    search_fields = ['name']
    ordering_fields = ['name']

    def get_queryset(self):
        return super().get_queryset().filter(shop_id=self.request.user.default_shop_id)

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())

        if self.request.method == 'GET':
            return self.serializer_class(*args, ref_name='category_list', **kwargs,
                                         fields=['id', 'name', 'parent', 'status', 'position', 'description',
                                                 'show_in_ecommerce'])
        return self.serializer_class(*args, ref_name='category_create', **kwargs,
                                     fields=['name', 'parent', 'description', 'position'])


@extend_schema(tags=['Category'])
class CategoryUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = ShopCategoryDynamicFieldsModelSerializer
    permission_classes = IsOwner,
