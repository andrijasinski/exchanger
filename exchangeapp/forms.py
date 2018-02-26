from django import forms

CURRENCY_CHOICES = [
    ('eur', 'EUR'),
    ('kzt', 'KZT'),
    ('bob', 'BOB')
]

class ExchangeForm(forms.Form):

    from_currency = forms.CharField(label='Exchange from', widget=forms.Select(choices=CURRENCY_CHOICES))
    to_currency = forms.CharField(label='Exchange to', widget=forms.Select(choices=CURRENCY_CHOICES))
    amount = forms.FloatField(label="Amount", min_value=0)

class HistoryForm(forms.Form):
    from_currency = forms.CharField(label='Exchange from', widget=forms.Select(choices=CURRENCY_CHOICES))
    to_currency = forms.CharField(label='Exchange to', widget=forms.Select(choices=CURRENCY_CHOICES))