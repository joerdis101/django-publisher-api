# Generated by Django 2.1.5 on 2019-02-02 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190202_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author_id',
            new_name='author',
        ),
    ]