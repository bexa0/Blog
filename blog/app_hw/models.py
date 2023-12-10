from django.db import models
from django.urls import reverse


class Post(models.Model):
    author_post = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description_post = models.TextField()
    quantity_likes = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.author_post} - {self.title}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})