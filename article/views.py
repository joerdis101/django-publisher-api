from django.http import HttpResponse
from django.template import loader
from django.forms.models import model_to_dict

from article.models import Article, Author, Category
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from article.serializers import UserSerializer, GroupSerializer, ArticleSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def index(request):
    template = loader.get_template('article/index.html')
    articles = Article.objects.all()
    context = {'articles': articles}

    return HttpResponse(template.render(context, request))


def detail(request, id):
    template = loader.get_template('article/detail.html')
    article = Article.objects.get(id=id)
    article = model_to_dict(article)
    context = {'article': article}

    return HttpResponse(template.render(context, request))


def author(request):
    template = loader.get_template('article/author.html')
    authors = Author.objects.all()
    context = {'authors': authors}

    return HttpResponse(template.render(context, request))


def author_detail(request, id):
    template = loader.get_template('article/author-detail.html')
    author = Author.objects.get(id=id)
    context = {'author': author}

    return HttpResponse(template.render(context, request))


def category(request):
    template = loader.get_template('article/category.html')
    categories = Category.objects.all()
    context = {'categories': categories}

    return HttpResponse(template.render(context, request))


def user(request):
    template = loader.get_template('article/user.html')
    users = User.objects.all()
    context = {'users': users}

    return HttpResponse(template.render(context, request))


