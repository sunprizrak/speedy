from modeltranslation.translator import register, TranslationOptions
from .models import PrivacyPolicy


@register(PrivacyPolicy)
class PrivacyPolicyTranslationOptions(TranslationOptions):
    fields = ('text',)