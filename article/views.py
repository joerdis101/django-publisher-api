from django.http import HttpResponse
from django.template import loader
from django.forms.models import model_to_dict

from article.models import Article, Author, Category
from django.contrib.auth.models import User


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


