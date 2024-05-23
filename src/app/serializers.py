from rest_framework import serializers

from .models import WeightCategory, AgeCategory, Application, ApplicationStatus, Competition


class WeightCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightCategory
        fields = "__all__"


class AgeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeCategory
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = "__all__"


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = "__all__"
