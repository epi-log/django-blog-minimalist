from django.views.generic import ListView
from blog.models import Article


# One example of django built-in class based view. Very useful for list all elements from a model.
class ArticleList(ListView):
    model = Article
    paginate_by = 2