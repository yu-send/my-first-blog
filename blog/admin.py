from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'author')
    list_filter = ['published_date']
    search_fields = ['text', 'title']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
