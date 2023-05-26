from .models import CargoModel
from rest_framework import serializers


class CargoSerializerList(serializers.ModelSerializer):
    class Meta:
        model = CargoModel
        fields = '__all__'


class CargoSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = CargoModel
        fields = ('weight', 'description',)

