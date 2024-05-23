from modeltranslation.translator import translator, TranslationOptions, register
from ..models import Country, Region, District


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('title',)
