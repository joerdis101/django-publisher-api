from django.contrib import admin

from article.models import Author, Article, Category, Media, MediaType, ArticleCategory, ArticleMedia, ArticleElementPosition

admin.site.register([Author, ArticleMedia, Article, ArticleCategory, Category, MediaType, Media, ArticleElementPosition])
