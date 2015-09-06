from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
	def __str__(self):
		return self.title
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User)
	content = models.TextField()
	dateCreated = models.DateTimeField(auto_now_add=True)
	dateUpdated = models.DateTimeField(auto_now=True)
	active = models.BooleanField()

class Album(models.Model):
	def __str__(self):
		return self.title
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=50)
	thumbnail = models.ImageField(upload_to='blog/thumbnail')
	dateCreated = models.DateTimeField(auto_now_add=True)
	dateUpdated = models.DateTimeField(auto_now=True)
	active = models.BooleanField()

class Photo(models.Model):
	album = models.ForeignKey(Album)
	photo = models.ImageField(upload_to='blog/photo/fullsize/')
	dateCreated = models.DateTimeField(auto_now_add=True)
	dateUpdated = models.DateTimeField(auto_now=True)