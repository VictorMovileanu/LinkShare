from django.http import Http404
from django.views.generic import ListView, TemplateView
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

from bookmarks.models import Bookmark, Category

client = Elasticsearch()


class CategoriesView(ListView):
    model = Category
    template_name = 'bookmarks/categories.html'
    context_object_name = 'categories'


class CategoryListView(ListView):
    model = Bookmark
    paginate_by = 10
    context_object_name = 'bookmarks'

    def get_queryset(self):
        qs = super(CategoryListView, self).get_queryset()
        qs = qs.filter(category_id=self.kwargs.get('pk'))
        return qs


class BookmarkListView(TemplateView):
    template_name = 'bookmarks/bookmark_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        ctx = super(BookmarkListView, self).get_context_data(**kwargs)

        # SEARCH
        s = Search(using=client, index='bookmarks-index').filter("term", category=self.kwargs.get('pk'))

        # QUERY
        q = self.request.GET.get('q', "")
        if q:
            # todo: pagination does not work with query?
            q = Q("multi_match", query=q, fields=['title'])
            s = s.query(q)

        # PAGINATION
        try:
            page = int(self.request.GET.get('page', 1))
        except ValueError:
            page = 1
        s = s[self.paginate_by*(page-1):self.paginate_by*page]

        # EXECUTE
        response = s.execute()
        if response.hits:
            ctx['bookmarks'] = response.hits
            return ctx
        else:
            raise Http404
