# Generated by Django 2.1.5 on 2019-02-02 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_category_mediatype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=500)),
                ('main_text', models.TextField()),
                ('teaser_text', models.TextField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('author_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Author')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('alt_text', models.CharField(max_length=200)),
                ('caption', models.CharField(max_length=200)),
                ('credentials', models.TextField(max_length=500)),
                ('src', models.CharField(max_length=200)),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.MediaType')),
            ],
        ),
        migrations.AddField(
            model_name='articlemedia',
            name='media_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Media'),
        ),
    ]
