from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'daily'
    i18n = True

    def items(self):
        return ['home', 'about', 'games']

    def location(self, item):
        return reverse(item)