from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)