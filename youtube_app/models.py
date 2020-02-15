from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d/')
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):

        return self.title
