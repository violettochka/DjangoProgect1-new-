from django.db import models
from django.urls import reverse
from django.contrib.auth  import get_user_model
UserModel = get_user_model()

class Article(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    autor = models.ForeignKey(UserModel, on_delete = models.CASCADE, related_name = 'article')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['id']


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    message = models.TextField()
    article = models.ForeignKey('Topic', on_delete = models.CASCADE, related_name = 'comment')
    autor = models.ForeignKey(UserModel, on_delete = models.CASCADE, related_name = 'comment')

    def __str__(self):
        self.message = self.message[:10]
        return self.message
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Topic(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    userModels = models.ManyToManyField(UserModel)
    Articles = models.ManyToManyField(Article)

 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

