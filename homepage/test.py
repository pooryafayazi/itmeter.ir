from django.contrib import admin
from .models import News  # فرض بر این است که مدل شما News نام دارد

class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = "-empty-"    
    verbose_name_plural = 'News'
    list_display = ["short_title", "author", "status", 'published_date']
    list_filter = ["status", 'published_date', "author"]
    search_fields = ["title", "content"]

    def short_title(self, obj):
        return obj.title[:35]
    short_title.short_description = 'title'

admin.site.register(News, NewsAdmin)