
from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view ,name='blog'),
    path('category/<str:cat_name>', blog_view ,name='category'),
    path('<str:post_id>', single_view ,name='single'),


] 
