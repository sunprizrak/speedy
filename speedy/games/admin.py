from django.contrib import admin
from .models import Game
from modeltranslation.admin import TranslationAdmin


@admin.register(Game)
class GameAdmin(TranslationAdmin):
    list_display = ('name', 'created')
