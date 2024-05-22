from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import UserProfile, DocumentType
from .serializers import UserProfileSerializer, DocumentTypeSerializer


class GetUserProfile(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['document_num', 'document_sr', 'pinfl', 'is_foreigner', 'birth_date']


class DocumentTypeList(ListAPIView):
    serializer_class = DocumentTypeSerializer
    queryset = DocumentType.objects.filter(status=True)
