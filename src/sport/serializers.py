from rest_framework import serializers

from .models import SportType


class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = "__all__"