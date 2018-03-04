[![Build Status](https://travis-ci.org/andrijasinski/exchanger.svg?branch=master)](https://travis-ci.org/andrijasinski/exchanger)

# EXCHANGER

## Description

The "EXCHANGER" app provides a currency exchange functionality between EUR, KZT, BOB and other currencies. App also allows the user to see cross rate changes between those currencies for the past two weeks (14 days).

You can try application on 

## Requirements

* Python
* PIP package manager
* Django
* Terminal

PS. Since this app is integrated with currencylayer.com service, stable internet connection is required.

## Installation from source code

### Before

Before running server or tests please run in your terminal:
```
$ pip3 install -r requirements.txt #install from requirements file 
```

Make sure you have set up enviroment variables `CURRENCY_LAYER_API_KEY` with your API key and `DJANGO_EXCHANGER_DEBUG` to `True` or `False`. 

### Run server
To run server please enter root directory and type in your terminal:
```
$ python3 manage.py runserver
```

### Run test
To run test please enter root directory and type in your terminal:
```
$ python3 manage.py test
```

## How to use

To test core functionality, please visit `127.0.0.1:8000/` for currency exchanger and `127.0.0.1:8000/history/` to check out cross rate changes. 

PS. URL's are active only when server is running. 

## Author
* Andri Jasinski (andri.jasinski@gmail.com)

## Notes
* App is tested and works correctly with Python 3.6.4, PIP 9, Django-admin 2.0.2, Ubuntu 17.10.
