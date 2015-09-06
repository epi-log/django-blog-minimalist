from django.views.generic import ListView
from blog.models import Article, Album, Photo
from django.views.generic import TemplateView

# One example of django built-in class based view. Very useful for list all elements from a model.
class ArticleList(ListView):
	model = Article
	paginate_by = 2

class AlbumList(ListView):
	model = Album

class HomeView(TemplateView):
	template_name = "home.html"

class PhotoList(ListView):
	def get(self, request, *args, **kwargs):
		_id = kwargs.get("id")
		self.queryset = Photo.objects.filter(album_id=_id)
		return super(PhotoList, self).get(request, *args, **kwargs)