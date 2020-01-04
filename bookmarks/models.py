from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=128)


class Bookmark(models.Model):
    url = models.URLField(max_length=2048)
    title = models.CharField(max_length=256)
    rating = models.FloatField(null=True)
    views = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
