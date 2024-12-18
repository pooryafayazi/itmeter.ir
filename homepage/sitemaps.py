from django.contrib import sitemaps
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from homepage.models import News

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["homepage:index", "homepage:about", "homepage:contact"]

    def location(self, item):
        return reverse(item)

class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return News.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date