"""blog_manipal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import ArticleList, AlbumList, HomeView, PhotoList
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', HomeView.as_view()),
    url(r'^admin', include(admin.site.urls)),
    url(r'^articles', ArticleList.as_view()),
    url(r'^albums', AlbumList.as_view()),
    url(r'^album/(?P<id>[0-9]+)/$', PhotoList.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
