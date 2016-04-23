# coding: utf-8
from django.conf.urls import url
from django.contrib import admin

from search_engine.views import (EstablishmentSearchTemplateview,
                                 EstablishmentListView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', EstablishmentSearchTemplateview.as_view()),
    url(r'^establishments/$', EstablishmentListView.as_view()),
    url(r'autocomplete', 'search_engine.views.autocomplete')
]
