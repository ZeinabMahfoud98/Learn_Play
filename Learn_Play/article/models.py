from django.db import models

# Create your models here.

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='article_photos/', blank=True, null=True)

    def __str__(self):
        return self.title
