from django import forms
from .currencies import Currencies

CURRENCY_CHOICES = [
    ('eur', 'EUR'),
    ('kzt', 'KZT'),
    ('bob', 'BOB')
]

currencies = Currencies()

class ExchangeForm(forms.Form):

    from_currency = forms.CharField(label='Exchange from', widget=forms.Select(choices=currencies.as_choices()))
    to_currency = forms.CharField(label='Exchange to', widget=forms.Select(choices=currencies.as_choices()))
    amount = forms.FloatField(label="Amount", min_value=0)

class HistoryForm(forms.Form):
    from_currency = forms.CharField(label='Exchange from', widget=forms.Select(choices=currencies.as_choices()))
    to_currency = forms.CharField(label='Exchange to', widget=forms.Select(choices=currencies.as_choices()))