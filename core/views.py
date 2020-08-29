from django.views.generic import ListView
from .requests_factory import RequestsFactory


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'gifs'

    def get_queryset(self, *args, **kwargs):
        search = ''
        if self.request.GET.get('q') is not None and self.request.GET.get('q') != '':
            search = self.request.GET.get('q')
        return RequestsFactory.indexPage(self, search)
