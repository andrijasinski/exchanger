from django.shortcuts import render
from . import exchanger


exch = exchanger.Exchanger()
try:
    exch.currency_live
except AttributeError:
    exch.get_live_currency()

def index(request):
    params = {
        'usd_eur': exch.usd_eur, 
        'usd_kzt': exch.usd_kzt, 
        'usd_bob': exch.usd_bob
    }
    return render(request, 'exchangeapp/home.html', {'exchanger_content': params})