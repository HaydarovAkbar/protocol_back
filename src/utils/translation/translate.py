from modeltranslation.translator import translator, TranslationOptions, register
from ..models import State, District, Region, Language, Category, Specialization, Instruction


@register(State)
class StateTranslationOptions(TranslationOptions):
    fields = ('name',)