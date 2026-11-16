from django.contrib.sitemaps import Sitemap
from .models import Post
from django.utils import timezone

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now())

    def location(self, obj):
        return obj.get_absolute_url()
    def lastmod(self, obj):
        return obj.published_date