from django import template
from homepage.models import News, newsComment
from blog.models import Category
register = template.Library()
from django.utils import timezone

@register.filter
def truncate_w(text, word_count):
    words = text.split()
    if len(words) > word_count:
        return ' '.join(words[:word_count]) + '...'
    return text


@register.simple_tag
def get_latest_news(count=6):
    return News.objects.order_by('-published_date')[:count].filter(status=1, published_date__lte=timezone.now())

@register.inclusion_tag('home/popular-news.html')
def latest_news(arg=3):
    news = News.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-counted_views')[:arg]
    return {'news' : news}


@register.simple_tag(name='comments_count')
def function(news_id):
    return newsComment.objects.filter(News=news_id, approved=True).count()

@register.inclusion_tag('blog/blog-News-category.html')
def postcategories():
    news = News.objects.filter(status=1, published_date__lte=timezone.now())
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = news.filter(category=name).count()
    return {'categories' : cat_dict}