from rest_framework.serializers import ModelSerializer


class DynamicFieldsModelSerializer(ModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            for field_name in set(self.fields) - set(fields):
                self.fields.pop(field_name)

        if exclude is not None:
            for field_name in set(exclude):
                self.fields.pop(field_name)
