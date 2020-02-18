from django.db import models
from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    post_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Comments(models.Model):

    post = models.ForeignKey(Post)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
