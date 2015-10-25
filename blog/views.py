from django.views.generic import ListView
from blog.models import Article, Comment
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages


# One example of django built-in class based view. Very useful for list all elements from a model.
class ArticleList(ListView):
    model = Article
    paginate_by = 2


def post_comment(request):
    if request.method == 'POST':
        if request.POST['_firstname'] and request.POST['_lastname'] and request.POST['_content'] and request.POST['_id_article']:
            firstname = request.POST['_firstname']
            lastname = request.POST['_lastname']
            content = request.POST['_content']
            article = get_object_or_404(Article, id=request.POST['_id_article'])
            comment = Comment(firstname=firstname, lastname=lastname, content=content, id_article=article)
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Votre commentaire a été posté avec succès.")
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Une erreur est survenue. Veuilliez réessayer plus tard ou contacter l'administrateur du site.")
        return HttpResponseRedirect('/')
    else:
        messages.add_message(request, messages.ERROR,
                             "Une erreur est survenue. Veuilliez réessayer plus tard ou contacter l'administrateur du site.")
        return HttpResponseRedirect('/')
