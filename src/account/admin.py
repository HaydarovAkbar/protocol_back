from django.contrib import admin

from .models import UserProfile, DocumentId, DocumentType

admin.site.register(UserProfile)
admin.site.register(DocumentType)
admin.site.register(DocumentId)
