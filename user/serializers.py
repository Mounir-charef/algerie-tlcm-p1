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

    @staticmethod
    def get_cmp_name(obj):
        return obj.cmp.name

    class Meta:
        model = models.Information
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super(InformationSerializer, self).to_representation(instance)
    #     rep['cmp'] = instance.cmp.name
    #     return rep


class InformationDotSerializer(ModelSerializer):
    dot_name = SerializerMethodField(source='get_dot_name')

    @staticmethod
    def get_dot_name(obj):
        return obj.dot.name

    class Meta:
        model = models.InformationDot
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super(InformationDotSerializer, self).to_representation(instance)
    #     rep['dot'] = instance.dot.name
    #     return rep
