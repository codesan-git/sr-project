from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'unit', 'published', 'author']
    search_fields = ['title']
    list_per_page = 8

admin.site.register(Article, ArticleAdmin)