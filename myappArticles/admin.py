from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'autor']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Topic)
