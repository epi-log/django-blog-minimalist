from django.contrib import admin
from blog.models import Article
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article)