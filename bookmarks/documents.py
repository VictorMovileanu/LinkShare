
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Integer

connections.create_connection(hosts=['localhost'])


class BookmarkIndex(Document):
    # todo: https://elasticsearch-dsl.readthedocs.io/en/latest/persistence.html
    url = Text()
    title = Text()
    views = Integer()
    category = Integer()

    class Index:
        name = 'bookmarks-index'
