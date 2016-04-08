# coding: utf-8
from django.conf.urls import url
from django.contrib import admin

from homesite.views import IndexSearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexSearchView.as_view())
]
