from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'autor']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'autor']
    ordering = ['id']

class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Topic, TopicAdmin)
