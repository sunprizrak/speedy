from django.views.generic import ListView
from .models import Game
from django.utils.translation import gettext_lazy as _


class GamesView(ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'games/games.html'
    extra_context = {
        'title': _('Games')
    }