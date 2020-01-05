from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView

from bookmarks.models import Bookmark, Category


class CategoriesView(ListView):
    model = Category
    template_name = 'bookmarks/categories.html'
    context_object_name = 'categories'


class CategoryListView(ListView):
    # todo: svg icons are not rendered in chrome
    #  probably an issue with mimetypes
    #  try out: https://stackoverflow.com/questions/2312714/can-the-django-dev-server-correctly-serve-svg
    model = Bookmark
    paginate_by = 10
    context_object_name = 'bookmarks'

    def get_queryset(self):
        qs = super(CategoryListView, self).get_queryset()
        qs = qs.filter(category_id=self.kwargs.get('pk'))
        return qs
