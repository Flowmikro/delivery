from rest_framework import serializers

from .models import TruckModel


class TruckSerializerList(serializers.ModelSerializer):
    class Meta:
        model = TruckModel
        fields = '__all__'


class TruckSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = TruckModel
        fields = ('zip',)