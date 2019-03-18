from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(max_length=1024)


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent_category = models.IntegerField()


class MediaType(models.Model):
    name = models.CharField(max_length=200)


class Media(models.Model):
    name = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=200)
    caption = models.CharField(max_length=200)
    credentials = models.TextField(max_length=500)
    src = models.CharField(max_length=200)
    type = models.ForeignKey(MediaType, on_delete=models.CASCADE)


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    headline = models.CharField(max_length=500)
    sub_headline = models.CharField(max_length=500, null=True)
    main_text = models.TextField()
    teaser_text = models.TextField(max_length=500)
    quote = models.CharField(max_length=500, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()


class ArticleCategory(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class ArticleMedia(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    weight = models.IntegerField()


class ArticleElementPosition(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.IntegerField(default=40)
    headline = models.IntegerField(default=1)
    sub_headline = models.IntegerField(default=10)
    main_text = models.IntegerField(default=20)
    teaser_text = models.IntegerField(default=10)
    quote = models.IntegerField(default=30)
    created = models.IntegerField(default=50)
    updated = models.IntegerField(default=50)
