from django.contrib import admin
from blog.models import Post,Category,Comment
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin


class PostAdmin (SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    #fields = [ "title"] #jjust these fildes can be edited in panel
    #exclude = ["birth_date"] #just these fildes cannot be edited
    list_display = ["short_title","author", "status",'login_require','published_date',"created_date"]
    list_filter =  ["status",'published_date',"author",]
    #ordering = ['-created_date']
    search_fields = ["title", "'content"]

    summernote_fields = ('content',)
    def short_title(self, obj):
        return obj.title[:35]+ "..."
    short_title.short_description = 'title'

 

class CommentAdmin (admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    #fields = [ "title"]
    #exclude = ["birth_date"]
    list_display = ["name","post", "approved","created_date",'updated_date']
    list_filter =  ["post",'updated_date',"approved",]
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
