# coding: utf-8
from django.views.generic import FormView

from .forms import EstablishmentForm


class IndexSearchView(FormView):
    form_class = EstablishmentForm
    template_name = 'homesite/index.html'
