'''
To render html web pages
'''
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    '''
    Take in a request (Django sends request)
    Return as a response (We pick  to return the response)
    '''
    number = random.randint(1, 5)
    name = 'Justin'

    #from database
    article_obj = Article.objects.get(id = number)
    article_queryset = Article.objects.all()

    context = {
        'object_list' : article_queryset,
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content,
    }

    HTML_STRINGS = render_to_string('home_view.html', context=context )

    return HttpResponse(HTML_STRINGS)