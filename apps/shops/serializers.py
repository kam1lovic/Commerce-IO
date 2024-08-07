from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from shared.django.serializers import DynamicFieldsModelSerializer
from shops.models import Shop, Language, Country
from users.models import Plan


class CountryModelSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = 'id', 'code'


class ShopModelSerializer(DynamicFieldsModelSerializer):
    languages = PrimaryKeyRelatedField(many=True, queryset=Language.objects.all())

    # owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Shop
        exclude = ('created_at', 'updated_at', 'plan', 'owner', 'services')

    def create(self, validated_data):
        request = self.context['request']
        languages_data = validated_data.pop('languages')
        shop = Shop.objects.create(
            owner=request.user,
            plan_id=Plan.objects.get(id=1).id,
            **validated_data

        )
        shop.languages.set(languages_data)

        user = request.user
        user.default_shop = shop
        user.save()

        return shop

    def to_representation(self, instance: Shop):
        representation = super().to_representation(instance)
        representation['country'] = CountryModelSerializer(instance.country).data
        return representation

# class CategoryListModelSerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
#
#
# class CategoryCreateModelSerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('name', 'emoji', 'parent', 'description', 'position')
#
#     def create(self, validated_data):
#         request = self.context['request']
#         user = get_object_or_404(User, pk=request.user.id)
#         validated_data['shop'] = user.default_shop
#         category = Category.objects.create(
#             **validated_data
#         )
#
#         return category
#
#
# class CategoryUpdateModelSerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('name', 'emoji', 'parent', 'description', 'position')
