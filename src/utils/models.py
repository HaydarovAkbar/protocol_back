from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    status = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)
        return self


class Country(BaseModel):
    title = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)

    code = models.CharField(max_length=10, null=True, blank=True)
    flag = models.CharField(max_length=255, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Countries'
        verbose_name = 'Country'
        db_table = 'country'


class Region(BaseModel):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Regions'
        verbose_name = 'Region'
        db_table = 'region'


class District(BaseModel):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Districts'
        verbose_name = 'District'
        db_table = 'district'
