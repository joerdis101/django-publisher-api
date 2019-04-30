import graphene

from graphene_django.types import DjangoObjectType

from redactioncms.article.models import Article, ArticleCategory, Author, Category, MediaType, ArticleElementPosition


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class ArticleCategoryType(DjangoObjectType):
    class Meta:
        model = ArticleCategory


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class MediaTypeType(DjangoObjectType):
    class Meta:
        model = MediaType


class ArticleElementPositionType(DjangoObjectType):
    class Meta:
        model = ArticleElementPosition


class Query(object):
    all_articles = graphene.List(ArticleType)
    all_authors = graphene.List(AuthorType)

    def resolve_all_articles (self):
        return Article.objects.all()

    def resolve_all_authors(self):
        return Author.objects.select_related('article').all()
