from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import SportType
from .serializers import SportTypeSerializer


class AgeCategoryList(ListAPIView):
    serializer_class = SportTypeSerializer
    queryset = SportType.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'attr']