from django import template
from blog.models import Post,Comment
register = template.Library()
from blog.models import Category
from django.utils import timezone