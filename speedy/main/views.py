from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.utils.translation import gettext_lazy as _
from .models import PrivacyPolicy


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


class PrivacyPolicyView(TemplateView):
    template_name = 'main/privacy_policy.html'
    extra_context = {
        'title': _('Privacy policy')
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug_from_url = self.kwargs.get('slug')
        context['privacy_policy'] = PrivacyPolicy.objects.filter(game_name=slug_from_url).first()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)