from django import template
from blog.models import Post,Comment
register = template.Library()
from blog.models import Category
from django.utils import timezone

@register.inclusion_tag('blog/popular-posts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-counted_views')[:arg]
    return {'posts' : posts}