# coding: utf-8
import re
import json

from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, TemplateView
from django.db.models import Q

from haystack.query import SearchQuerySet

from search_engine.forms import EstablishmentForm
from search_engine.models import AvailabilityEstablishment


class SearchFormView(object):
    def get_context_data(self, **kwargs):
        context = super(SearchFormView, self).get_context_data(**kwargs)
        context['form'] = EstablishmentForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = context['form']
        if form.is_valid():
            request.session['values_post'] = form.cleaned_data
            form.cleaned_data['checkin'] = form.cleaned_data[
                'checkin'].strftime('%Y-%m-%d')
            form.cleaned_data['checkout'] = form.cleaned_data[
                'checkout'].strftime('%Y-%m-%d')
            return HttpResponseRedirect('establishments/')
        return super(SearchFormView,
                     self).render_to_response(context)


class EstablishmentSearchTemplateview(SearchFormView, TemplateView):
    template_name = 'search_engine/index.html'


class EstablishmentListView(ListView):
    model = AvailabilityEstablishment
    template_name = 'search_engine/establishments.html'
    context_object_name = 'establishments'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(EstablishmentListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = SearchQuerySet().all()
        values = self.request.session.get('values_post')
        return queryset.filter(available=True,
                               name=values.get('name').split('-')[1].strip())

    def get_querystring_url(self):
        querystring = self.request.GET.urlencode()
        _query = re.sub(r'&?page=\d+', '', querystring)
        return '?%s' % _query if _query else '?'


def autocomplete(request):
    term = request.GET.get('term')
    sqs = SearchQuerySet().filter(
        Q(name__icontains=term) | Q(city__icontains=term) |
        Q(city__startswith=term) | Q(name__startswith=term))
    sugestoes = [(dict(
        name=resultado.name,
        city=resultado.city,
    )) for resultado in sqs]
    data = json.dumps(sugestoes)
    return HttpResponse(data, content_type='application/json')
