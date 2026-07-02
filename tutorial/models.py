from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="tile")
    author = models.CharField(max_length=150, verbose_name="author")
    description = models.TextField(blank=True, null=True, verbose_name="description")
    published_date = models.DateField(blank=True, null=True, verbose_name="published_date")
    price = models.IntegerField(default=0, verbose_name="price")

    def __str__(self):
        return self.title