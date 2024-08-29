from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import ListAPIView

from shared.restframework.paginations import CustomPagination
from shops.models.categories import Category
from shops.serializers.category import ShopCategoryDynamicFieldsModelSerializer


@extend_schema(tags=['Category'])
@extend_schema_view(
    list=extend_schema(
        responses=ShopCategoryDynamicFieldsModelSerializer(ref_name='category_list', fields=['id', 'name'])))
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ShopCategoryDynamicFieldsModelSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return super().get_queryset().filter(shop_id=self.request.user.default_shop_id)

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())
        if self.request.method == 'GET':
            return self.serializer_class(*args, ref_name='category_list', **kwargs,
                                         fields=['id', 'name'])
        return super().get_serializer(*args, **kwargs)
