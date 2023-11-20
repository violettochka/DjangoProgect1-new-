from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def article(request, article):
    return HttpResponse(f'Presentation of parts of one article. Article consist dinamic part: {article}')

def article_comment(reguest, article):
    return HttpResponse(f'Here you can add your comment. Article consist dinamic part: {article}')    

def article_update(request, article):
    return HttpResponse(f'Here you can update article on the site. Article consist dinamic part: {article}')    

def article_delete(request, article):
    return HttpResponse(f'Here you can delete article on the site. Article consist dinamic part: {article}')


def topics(request):
    return HttpResponse('List of available themes on the site')

def topics_subscribe(request, topic):
    return HttpResponse(f'views for subscribing to a topic. Your topic: {topic}')

def topics_unsubscribe(request, topic):
    return HttpResponse(f'views for unsubscribing to a topic. Your topic: {topic}')
