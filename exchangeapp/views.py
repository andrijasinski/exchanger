from django.shortcuts import render
from .exchanger import Exchanger
from .forms import ExchangeForm
from django.http import HttpResponseRedirect


exch = Exchanger()
try: 
    exch.currency_live
except AttributeError:
    exch.get_live_currency()

def index(request):
    return HttpResponseRedirect('/exchange/?from=eur&to=kzt&amount=0')

def form(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            from_curr = form.cleaned_data["from_currency"]
            to_curr = form.cleaned_data["to_currency"]
            amt = form.cleaned_data["amount"]

            return HttpResponseRedirect('/exchange/?from={}&to={}&amount={}'.format(from_curr, to_curr, amt))

    else:
        form = ExchangeForm(initial={
            'from_currency': request.GET.get('from', 'eur'),
            'to_currency': request.GET.get('to', 'kzt'),
            'amount': request.GET.get('amount', 0)
            })

    return render(request, 'exchangeapp/name.html', {'form': form})