from django.contrib import admin
from django.urls import path
from homepage.views import *

app_name = 'homepage'

urlpatterns = [
    path('', index_view ,name='index'),
    path('about', about_view,name='about' ),
    path('contact', contact_view ,name='contact'),

] 
