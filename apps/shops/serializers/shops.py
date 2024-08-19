from rest_framework.fields import CurrentUserDefault, HiddenField
from rest_framework.generics import get_object_or_404
from rest_framework.relations import PrimaryKeyRelatedField
from shared.django.serializers import DynamicFieldsModelSerializer
from shops.models import Language, Shop
from shops.serializers.others import CountryModelSerializer
from users.models import Plan


class ShopDynamicFieldsModelSerializer(DynamicFieldsModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())
    languages = PrimaryKeyRelatedField(many=True, queryset=Language.objects.all())

    class Meta:
        model = Shop
        fields = '__all__'

    def create(self, validated_data):
        validated_data['plan'] = get_object_or_404(Plan, code='free')
        user = self.context['request'].user
        shop = Shop.objects.create(**validated_data)
        user.default_shop = shop
        user.save()
        return shop

    def to_representation(self, instance: Shop):
        representation = super().to_representation(instance)
        representation['country'] = CountryModelSerializer(instance.country).data
        return representation
