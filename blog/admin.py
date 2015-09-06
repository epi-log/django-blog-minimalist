from django.contrib import admin
from blog.models import Article, Album, Photo
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)