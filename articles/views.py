from cgitb import lookup
from turtle import title
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import ArticleForm
from .models import Article

# Create your views here.
# def article_search_view(request):
#     query_dict = request.GET #this a dictionary
#     try:
#         query =int(query_dict.get('q'))
#     except:
#         query=None

#     article_obj = None
#     if query is not None:
#         article_obj = Article.objects.get(id=query)
#     context={
#         'object' : article_obj
#     }
#     return render(request, 'articles/search.html', context=context)

def article_search_view(request):
    query = request.GET.get('q') #this a dictionary
    qs = Article.objects.all()
    if query is not None:
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        qs = Article.objects.filter(lookups)
    context={
        'object_list' : qs
    }
    return render(request, 'articles/search.html', context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        # return redirect("article-detail", slug=article_object.slug)
        return redirect(article_object.get_absolute_url())
        # title = form.cleaned_data['title']
        # content = form.cleaned_data['content']
        # article_object = Article.objects.create(title=title, content=content)
        # context['object']=article_object
        # context['created']=True
    return render(request, 'articles/create.html',  context=context)


def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first
        except:
            raise Http404 
    context = {
        "objects": article_obj
    }

    return render(request, 'articles/detail.html',  context=context)