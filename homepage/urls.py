from django.contrib import admin
from django.urls import path
from homepage.views import *

app_name = 'homepage'

urlpatterns = [
    path('', index_view ,name='index'),
    path('about', about_view,name='about' ),
    path('contact', contact_view ,name='contact'),
    path('newsletter', newsletter_view ,name='newsletter'),
    path('<str:news_id>', single_news ,name='news'),
    path('news/category/<str:cat_name>', index_view ,name='category'),
    path('author/<str:author>', index_view ,name='author'),
    path('search/', index_search, name='search'),

] 
