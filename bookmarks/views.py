from django.views.generic import ListView, TemplateView
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

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
        s = Search(index='bookmarks-index').query("match", category=self.kwargs.get('pk'))
        try:
            page = int(self.request.GET.get('page', 1))
        except ValueError:
            page = 1
        s = s[self.paginate_by*(page-1):self.paginate_by*page]
        response = s.execute()
        ctx['bookmarks'] = response.hits
        return ctx
