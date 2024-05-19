from django.db import models
from django.utils import timezone

from utils.models import BaseModel


class SportType(BaseModel):
    name = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(SportType, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = 'Sport Types'
        verbose_name = 'Sport Type'
        db_table = 'sport_type'
