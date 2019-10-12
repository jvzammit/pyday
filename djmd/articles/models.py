from django.db import models
from django.urls import reverse


class Article(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=256)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
