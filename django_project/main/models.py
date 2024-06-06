# main/models.py

from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='news_comments', null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.news.title}'
