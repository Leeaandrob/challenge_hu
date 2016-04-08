# coding: utf-8
import re

from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.db.models import Q

from search_engine.forms import EstablishmentForm
from search_engine.models import Establishment


class SearchFormView(object):
    def get_context_data(self, **kwargs):
        context = super(SearchFormView, self).get_context_data(**kwargs)
        context['form'] = EstablishmentForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context['form'].is_valid():
            name = context['form'].cleaned_data['name']
            request.session['values_post'] = name
            return HttpResponseRedirect('establishments/')
        return super(SearchFormView,
                     self).render_to_response(context)


class EstablishmentSearchTemplateview(SearchFormView, TemplateView):
    template_name = 'homesite/index.html'


class EstablishmentListView(ListView):
    model = Establishment
    template_name = 'homesite/establishments.html'
    context_object_name = 'establishments'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(EstablishmentListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = Establishment.objects.all()
        values = self.request.session.get('values_post')
        return queryset.filter(name__icontains=values)

    def get_querystring_url(self):
        querystring = self.request.GET.urlencode()
        _query = re.sub(r'&?page=\d+', '', querystring)
        return '?%s' % _query if _query else '?'
