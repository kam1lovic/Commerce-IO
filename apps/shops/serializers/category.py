from shared.restframework.serializers import DynamicFieldsModelSerializer
from shops.models import ShopCategory
from shops.models.categories import Category


class ShopCategoryDynamicFieldsModelSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ShopCategory
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['shop'] = user.default_shop
        category = Category.objects.create(**validated_data)
        return category
