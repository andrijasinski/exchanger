from django.shortcuts import render
from .exchanger import Exchanger
from .forms import UserForm, NameForm
from django.http import HttpResponseRedirect


exch = Exchanger()
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
    return render(request, 'exchangeapp/header.html', {'exchanger_content': params})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        print("=============", request.method)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'exchangeapp/name.html', {'form': form})