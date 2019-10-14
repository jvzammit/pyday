# articles/admin.py
from django.contrib import admin
from django.db import models

from markdownx.widgets import AdminMarkdownxWidget

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }


admin.site.register(Article, ArticleAdmin)
