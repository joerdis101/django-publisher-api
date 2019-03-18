"""redactioncms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article.views import index as article_index
from article.views import detail
from article.views import author
from article.views import author_detail
from article.views import category
from article.views import user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', article_index),
    path('articles/<int:id>', detail),
    path('articles/<int:id>/<int:year>', detail),
    path('authors/', author),
    path('authors/<int:id>', author_detail),
    path('categories/', category),
    path('users/', user)
]