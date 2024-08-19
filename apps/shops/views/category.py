from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from shared.restframework.permissions import IsOwnerCategory
from shops.models import Category
from shops.serializers.category import CategoryDynamicFieldsModelSerializer


@extend_schema(tags=['Category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDynamicFieldsModelSerializer

    def get_queryset(self):
        return super().get_queryset().filter(shop_id=self.request.user.default_shop_id)

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())

        if self.request.method == 'GET':
            return self.serializer_class(*args, **kwargs,
                                         fields=['emoji', 'name', 'parent', 'status', 'show_in_commerce'])
        return self.serializer_class(*args, **kwargs,
                                     fields=['name', 'parent', 'emoji', 'description', 'position', 'image'])


@extend_schema(tags=['Category'])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDynamicFieldsModelSerializer
    permission_classes = IsOwnerCategory,
