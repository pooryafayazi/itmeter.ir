from django.contrib import admin
from .models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name', 'email', 'created_date']
    list_filter = ['email']
    search_fields = ['name', 'message']

class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = "-empty-"    
    verbose_name_plural = 'News'
    #fields = [ "title"]
    #exclude = ["birth_date"]
    list_display = ["title","author", "status",'published_date']
    list_filter =  ["status",'published_date',"author",]
    #ordering = ['-created_date']
    search_fields = ["title", "'content"]

    #summernote_fields = ('content',)

class NewsCommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    #fields = [ "title"]
    #exclude = ["birth_date"]
    list_display = ["name","news", "approved","created_date",'updated_date']
    list_filter =  ["news",'updated_date',"approved",]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
admin.site.register(News, NewsAdmin)
admin.site.register(Topic)
admin.site.register(newsComment, NewsCommentAdmin)
