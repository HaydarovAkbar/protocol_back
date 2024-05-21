from django.db import models
from django.utils import timezone

from utils.models import BaseModel
from sport.models import SportType


class Competition(BaseModel):
    title = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)
    sport_type = models.ForeignKey(SportType, on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Competitions'
        verbose_name = 'Competition'
        db_table = 'competition'
