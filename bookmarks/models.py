from django.db import models

from bookmarks.documents import BookmarkIndex


class Category(models.Model):
    title = models.CharField(max_length=128)


class Bookmark(models.Model):
    url = models.URLField(max_length=2048)
    title = models.CharField(max_length=256)
    rating = models.FloatField(null=True)
    views = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def indexing(self):
        obj = BookmarkIndex(
            meta={'id': self.id},
            url=self.url,
            title=self.title,
            views=self.views,
            category=getattr(self.category, 'pk', None),
        )
        obj.save()
        return obj.to_dict(include_meta=True)
