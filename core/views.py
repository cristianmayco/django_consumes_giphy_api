from django.views.generic import ListView
from .requests_factory import RequestsFactory


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'gifs'

    def get_queryset(self):
        return RequestsFactory.indexPage(self)