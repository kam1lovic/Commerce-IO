from shared.django.serializers import DynamicFieldsModelSerializer
from shops.models import Category


class CategoryDynamicFieldsModelSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Category
        exclude = ('id', 'created_at', 'updated_at', 'position', 'shop')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['shop'] = user.default_shop
        category = Category.objects.create(**validated_data)
        return category
