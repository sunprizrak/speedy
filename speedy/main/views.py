from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class HomeView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Yodcomedia'
    }


class AboutUsView(TemplateView):
    template_name = 'main/about_us.html'
    extra_context = {
        'title': _('About')
    }

