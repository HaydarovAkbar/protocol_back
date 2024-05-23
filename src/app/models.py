from django.db import models
from django.utils import timezone

from utils.models import BaseModel
from sport.models import SportType


class WeightCategory(BaseModel):
    title = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)
    sport_type = models.ForeignKey(SportType, on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Weight Categories'
        verbose_name = 'Weight Category'
        db_table = 'weight_category'


class AgeCategory(BaseModel):
    title = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)
    sport_type = models.ForeignKey(SportType, on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Age Categories'
        verbose_name = 'Age Category'
        db_table = 'age_category'


class Competition(BaseModel):
    title = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)
    sport_type = models.ForeignKey(SportType, on_delete=models.SET_NULL, null=True, blank=True)

    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Competitions'
        verbose_name = 'Competition'
        db_table = 'competition'


class ApplicationStatus(BaseModel):
    title = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Application Statuses'
        verbose_name = 'Application Status'
        db_table = 'application_status'


class Application(BaseModel):
    user = models.ForeignKey('account.UserProfile', on_delete=models.SET_NULL, null=True, blank=True)
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, null=True, blank=True)
    weight_category = models.ForeignKey(WeightCategory, on_delete=models.SET_NULL, null=True, blank=True)
    age_category = models.ForeignKey(AgeCategory, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(ApplicationStatus, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural = 'Applications'
        verbose_name = 'Application'
        db_table = 'application'
        indexes = [
            models.Index(fields=['user_id', 'competition_id', 'weight_category_id', 'age_category_id'])
        ]
