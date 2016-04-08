# coding: utf-8
from django import forms


class EstablishmentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Search by Name'}))
    checkin = forms.DateField()
    checkout = forms.DateField()
