from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=1500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title