from rest_framework.serializers import ModelSerializer

from .models import UserProfile, DocumentType


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class DocumentTypeSerializer(ModelSerializer):
    class Meta:
        model = DocumentType
        fields = "__all__"
