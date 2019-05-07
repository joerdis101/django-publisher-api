import graphene

from graphene_django.types import DjangoObjectType

from article.models import Article, Author


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class Query(object):
    all_articles = graphene.List(ArticleType)
    all_authors = graphene.List(AuthorType)

    @staticmethod
    def resolve_all_articles(*args, **kwargs):
        return Article.objects.all()

    @staticmethod
    def resolve_all_authors(*args, **kwargs):
        return Author.objects.select_related('article').all()
