from modeltranslation.translator import register, TranslationOptions
from .models import Game


@register(Game)
class GameTranslationOptions(TranslationOptions):
    fields = ('name', 'description')