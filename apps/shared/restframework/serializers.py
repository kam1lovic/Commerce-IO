from drf_spectacular.extensions import OpenApiSerializerExtension
from rest_framework.serializers import ModelSerializer


class DynamicFieldsModelSerializer(ModelSerializer):
    def __init__(self, *args, ref_name=None, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        self.ref_name = ref_name
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude is not None:
            exclude_fields = set(exclude)
            for field_name in exclude_fields:
                self.fields.pop(field_name)


class DynamicFieldsModelSerializerExtension(OpenApiSerializerExtension):
    target_class = DynamicFieldsModelSerializer  # this can also be an import string
    match_subclasses = True

    def map_serializer(self, auto_schema, direction):
        return auto_schema._map_serializer(self.target, direction, bypass_extensions=True)

    def get_name(self, auto_schema, direction):
        return self.target.ref_name
