# coding: utf-8
from django.conf.urls import url
from django.contrib import admin

from homesite.views import (EstablishmentSearchTemplateview,
                            EstablishmentListView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', EstablishmentSearchTemplateview.as_view()),
    url(r'^establishments/$', EstablishmentListView.as_view()),
    url(r'autocomplete', 'homesite.views.autocomplete')
]
