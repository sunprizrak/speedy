from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import PrivacyPolicy


@admin.register(PrivacyPolicy)
class ArtistAdmin(TranslationAdmin):
    pass
