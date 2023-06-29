from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=250)
    date_created = models.DateTimeField(default=timezone.now())
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    time_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    content = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.content
