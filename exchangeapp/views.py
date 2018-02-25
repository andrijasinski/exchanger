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
    return HttpResponseRedirect('/exchange/?from=eur&to=kzt&amount=1')

def form(request):
    result = 0
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            from_curr = form.cleaned_data["from_currency"]
            to_curr = form.cleaned_data["to_currency"]
            amt = form.cleaned_data["amount"]
            return HttpResponseRedirect('/exchange/?from={}&to={}&amount={}'.format(from_curr, to_curr, amt))

    else:
        from_curr = request.GET.get('from', 'eur')
        to_curr = request.GET.get('to', 'kzt')
        amt = request.GET.get('amount', 1)
        form = ExchangeForm(initial={
            'from_currency': from_curr,
            'to_currency': to_curr,
            'amount': amt
            })
        result = exch.exchange(from_curr, to_curr, float(amt))

    return render(request, 'exchangeapp/exchanger_form.html', {'form': form, 'exchange_result': result})

def history(request):
    return render(request, 'exchangeapp/history.html')
