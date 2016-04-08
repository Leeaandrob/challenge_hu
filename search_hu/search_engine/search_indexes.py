# coding: utf-8
from haystack import indexes
from search_engine.models import Establishment


class EstablishmentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    city = indexes.CharField(model_attr='city')
    content_auto = indexes.EdgeNgramField()

    def get_model(self):
        return Establishment

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
