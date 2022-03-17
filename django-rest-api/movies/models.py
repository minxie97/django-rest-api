from django.db import models
from django.contrib.auth import get_user_model

class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    description = models.TextField()
    watcher = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title