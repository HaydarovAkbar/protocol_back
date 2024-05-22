from django.db import models

from utils.models import BaseModel


class DocumentType(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class DocumentId(BaseModel):
    title = models.CharField(max_length=255)
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class UserProfile(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True)
    document_sr = models.ForeignKey(DocumentId, on_delete=models.SET_NULL, null=True, blank=True)
    document_num = models.PositiveIntegerField(null=True, blank=True)
    pinfl = models.CharField(max_length=14, null=True, blank=True)

    is_foreigner = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
        db_table = 'user_profile'
        indexes = [
            models.Index(fields=['pinfl', 'document_num', 'document_sr_id', 'birth_date'])
        ]
