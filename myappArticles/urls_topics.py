from django.urls import path
from .views import topics, topics_subscribe, topics_unsubscribe
urlpatterns = [
    path('', topics, name='topics'),
    path('<topic>/subscribe/', topics_subscribe ),
    path('<topic>/unsubscribe/', topics_unsubscribe),


]