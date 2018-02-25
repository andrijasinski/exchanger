from django import forms

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
]

CURRENCY_CHOICES = [
    ('eur', 'EUR'),
    ('kzt', 'KZT'),
    ('bob', 'BOB')
]

class ExchangeForm(forms.Form):

    from_currency = forms.CharField(label='Exchange from', widget=forms.Select(choices=CURRENCY_CHOICES))
    to_currency = forms.CharField(label='Exchange to', widget=forms.Select(choices=CURRENCY_CHOICES))
    amount = forms.FloatField(label="Amount")
    # def __init__(self, from_curr, to_curr, amt, *args, **kwargs): 
    #     super(ExchangeForm, self).__init__(*args, **kwargs)
    #     ExchangeForm.from_currency = forms.CharField(label='Exchange from', widget=forms.Select(choices=CURRENCY_CHOICES), initial=from_curr)
    #     ExchangeForm.to_currency = forms.CharField(label='Exchange to', widget=forms.Select(choices=CURRENCY_CHOICES), initial=to_curr)
    #     ExchangeForm.amount = forms.FloatField(label="Amount", initial=amt)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    redirect = '/thanks'