from django.shortcuts import render
from .exchanger import Exchanger
from .forms import ExchangeForm, HistoryForm
from django.http import HttpResponseRedirect
import arrow


exch = Exchanger()

def index(request):
    try: 
        exch.currency_live
    except AttributeError:
        exch.get_live_currency()
        
    return HttpResponseRedirect('/exchange/?from=eur&to=kzt&amount=1')

def exchanger_form(request):
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

    return render(request, 'exchangeapp/exchanger_form.html', {'form': form, 'exchange_result': round(result, 2)})

def history(request):
    try:
        exch.two_week_history
    except AttributeError:
        exch.get_two_week_history()

    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            from_curr = form.cleaned_data["from_currency"]
            to_curr = form.cleaned_data["to_currency"]
            return HttpResponseRedirect('/history/?from={}&to={}'.format(from_curr, to_curr))

    else:
        from_curr = request.GET.get('from', 'eur')
        to_curr = request.GET.get('to', 'kzt')
        form = HistoryForm(initial={
            'from_currency': from_curr,
            'to_currency': to_curr
            })
        changes, current = cross_rate_changes(from_curr, to_curr)

    return render(request, 'exchangeapp/history.html', {'form': form, 'changes': changes, 'current': round(current, 5)})

def cross_rate_changes(from_curr, to_curr):
    changes = {}
    for i in range(1, 15):
        arrow_obj = arrow.now().shift(days=-i)
        rate = exch.exchange(from_curr, to_curr, 1, arrow_obj.format('MMM DD, YYYY'))
        changes[arrow_obj.format('MMM DD, YYYY')] = round(rate, 5)
    return [changes, exch.exchange(from_curr, to_curr, 1)]