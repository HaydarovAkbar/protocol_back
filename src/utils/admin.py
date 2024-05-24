from django.contrib import admin
from .models import Country, District

admin.site.register(District)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'created_at', 'updated_at')
    search_fields = ('title', 'code')
    list_filter = ('title', 'code')
    ordering = ('-created_at',)


admin.site.register(Country, CountryAdmin)