from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch

from django.core.management.base import BaseCommand, CommandError

from bookmarks import documents, models
from bookmarks.models import Bookmark


class Command(BaseCommand):
    help = 'Index current bookmarks in the relational database'

    def handle(self, *args, **options):
        """
        test success with following curl command:

        curl - X GET "localhost:9200/_search?pretty" - H 'Content-Type: application/json' - d
        '
        {
            "query": {
                "match_all": {}
            }
        }
        '
        """
        documents.BookmarkIndex.init()
        es = Elasticsearch()
        bulk(client=es, actions=(b.indexing() for b in Bookmark.objects.all()))
