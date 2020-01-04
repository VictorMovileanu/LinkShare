from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class CategoryView(TemplateView):
    template_name = 'categories.html'
