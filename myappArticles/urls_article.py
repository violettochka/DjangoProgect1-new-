from django.urls import path
from .views import article, article_comment, article_update, article_delete

urlpatterns = [
    path('', article),
    path('comment/', article_comment),
    path('update/', article_update),
    path('delete/', article_delete),

]