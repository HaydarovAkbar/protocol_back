from django.contrib import admin

from .models import WeightCategory, AgeCategory, Application, ApplicationStatus, Competition

admin.site.register(WeightCategory)
admin.site.register(AgeCategory)
admin.site.register(Application)
admin.site.register(ApplicationStatus)
admin.site.register(Competition)
