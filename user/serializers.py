from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . import models


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'dot']


class DotSerializer(ModelSerializer):
    class Meta:
        model = models.Dot
        fields = '__all__'


class CmpSerializer(ModelSerializer):
    class Meta:
        model = models.Cmp
        fields = '__all__'


class InformationSerializer(ModelSerializer):
    cmp_name = SerializerMethodField(source='get_cmp_name')

    def get_cmp_name(self, obj):
        return obj.cmp.name

    class Meta:
        model = models.Information
        fields = '__all__'


class InformationDotSerializer(ModelSerializer):
    # region = StringRelatedField(many=False)

    class Meta:
        model = models.InformationDot
        fields = '__all__'
