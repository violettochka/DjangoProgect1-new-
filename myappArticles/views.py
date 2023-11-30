from django.shortcuts import render

from django.http import HttpResponse
from myappAccount.views import menu
from .models import *
# Create your views here.
def article(request, article):
    return HttpResponse(f'Presentation of parts of one article. Article consist dinamic part: {article}')

def article_comment(reguest, article):
    return HttpResponse(f'Here you can add your comment. Article consist dinamic part: {article}')    

def article_update(request, article):
    return HttpResponse(f'Here you can update article on the site. Article consist dinamic part: {article}')    

def article_delete(request, article):
    return HttpResponse(f'Here you can delete article on the site. Article consist dinamic part: {article}')


def topics(request,blog_id):
    topics= Topic.objects.filter(Articles = blog_id)
    context = {
        'topics':topics,
        'menu': menu
    }
    return render(request, 'myappAccount/topics.html', context=context)

def topics_subscribe(request, topic):
    return HttpResponse(f'views for subscribing to a topic. Your topic: {topic}')

def topics_unsubscribe(request, topic):
    return HttpResponse(f'views for unsubscribing to a topic. Your topic: {topic}')
