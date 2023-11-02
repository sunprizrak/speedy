from django.contrib import admin
from .models import PrivacyPolicy


@admin.register(PrivacyPolicy)
class ArtistAdmin(admin.ModelAdmin):
    pass
