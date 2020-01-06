from elasticsearch_dsl import analyzer, tokenizer
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Integer

from bookmarks.models import Bookmark
from . import abstract_index

connections.create_connection(hosts=['localhost'])

# from https://elasticsearch-dsl.readthedocs.io/en/latest/persistence.html
my_analyzer = analyzer('my_analyzer',
                       tokenizer=tokenizer('trigram', 'nGram', min_gram=3, max_gram=3),
                       filter=['lowercase']
                       )


class BookmarkIndex(abstract_index.DocumentBase):
    """
    inspired by https://medium.com/@harshvb7/managing-elasticsearch-in-django-like-a-pro-adfcd984920d
    """
    url = Text()
    title = Text(analyzer=my_analyzer)
    views = Integer()
    category = Integer()

    class Index:
        name = 'bookmarks-index'

    def get_model(self):
        return Bookmark

    def get_index_queryset(self):
        return self.get_model().objects.all()

    def create_document_dict(self, obj):
        # required (?)
        self.obj = obj

        doc = self.__class__(
            url=obj.url,
            title=obj.title,
            views=obj.views,
            category=getattr(obj.category, 'pk', None)
        )
        doc.meta.id = obj.id
        return doc.to_dict(include_meta=True)
