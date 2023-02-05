from rest_framework.serializers import ModelSerializer
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
    class Meta:
        model = models.Information
        fields = '__all__'


class InformationDotSerializer(ModelSerializer):
    class Meta:
        model = models.InformationDot
        fields = '__all__'