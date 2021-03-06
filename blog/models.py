from importlib.resources import contents
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    poster = models.CharField(max_length=50, default='anonymous')
    contents = models.CharField(max_length=1500)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(Post):
    post_id = models.IntegerField()