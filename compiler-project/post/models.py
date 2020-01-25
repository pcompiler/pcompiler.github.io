from django.db import models

from datetime import datetime

class Post(models.Model):
    
    title = models.CharField(max_length=64)
    text = models.TextField(blank=True)
    tag = models.CharField(max_length=64)

    creadted_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
