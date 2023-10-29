from rest_framework import serializers
from .models import Violin


class ViolinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violin
        fields = '__all__'
