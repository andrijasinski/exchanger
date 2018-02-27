from django.test import TestCase
from .exchanger import Exchanger
# from django.core.urlresolvers import reverse


class ExchangeTest(TestCase):

    exch = Exchanger()

    def test_homepage_url_exists_and_redirects(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/exchange/?from=eur&to=kzt&amount=1')

    def test_exchange_url_exists(self):
        resp = self.client.get('/exchange/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exchangeapp/exchanger_form.html')
    
    def test_exchange_url_with_right_params(self):
        ExchangeTest.exch.get_live_currency()
        resp = self.client.get('/exchange/?from=kzt&to=bob&amount=20')
        self.assertEqual(resp.status_code, 200)
        res = self.__class__.exch.exchange('kzt', 'bob', 20)
        self.assertEqual(resp.context['exchange_result'], round(res, 3))

    def test_exchange_url_with_wrong_currency(self):
        pass