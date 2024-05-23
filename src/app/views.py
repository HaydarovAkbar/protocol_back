from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import AgeCategory, WeightCategory, Competition, Application, ApplicationStatus
from .serializers import AgeCategorySerializer, WeightCategorySerializer, CompetitionSerializer, ApplicationSerializer, \
    ApplicationStatusSerializer
from pagination import TenPagination


class AgeCategoryList(ListAPIView):
    serializer_class = AgeCategorySerializer
    queryset = AgeCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'attr', 'sport_type']


class WeightCategoryList(ListAPIView):
    serializer_class = WeightCategorySerializer
    queryset = WeightCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'attr', 'sport_type']


class CompetitionList(ListAPIView):
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'attr', 'sport_type', 'user']
    authentication_classes = [IsAuthenticated]
    pagination_class = TenPagination

    def get_queryset(self):
        user = self.request.user
        return Competition.objects.filter(user=user)


class ApplicationList(ListAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'attr', 'competition', 'status', 'user']
    pagination_class = TenPagination


class ApplicationStatusList(ListAPIView):
    serializer_class = ApplicationStatusSerializer
    queryset = ApplicationStatus.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'attr']
    pagination_class = TenPagination
