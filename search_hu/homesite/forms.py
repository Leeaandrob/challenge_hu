# coding: utf-8
from django import forms


class EstablishmentForm(forms.Form):
    title = forms.CharField()
