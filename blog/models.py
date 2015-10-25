from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import formats


# Create your models here.

class Article(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    content = RichTextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    album = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-dateCreated']


class Comment(models.Model):
    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' ' + str(
            formats.date_format(self.dateCreated, "SHORT_DATETIME_FORMAT"))

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    content = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    id_article = models.ForeignKey(Article)
