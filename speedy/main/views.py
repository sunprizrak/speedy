from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Home page'
    }


class AboutUs(TemplateView):
    template_name = 'main/about_us.html'
    extra_context = {
        'title': 'About page'
    }


class Games(TemplateView):
    template_name = 'main/games.html'
    extra_context = {
        'title': 'Games'
    }
