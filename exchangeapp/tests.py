from django.test import TestCase
from .exchanger import Exchanger
import arrow


class ExchangeTest(TestCase):

    exch = Exchanger()
    exch.get_live_currency()

    def test_homepage_url_exists_and_redirects(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/exchange/?from=eur&to=kzt&amount=1')

    def test_exchange_url_exists(self):
        resp = self.client.get('/exchange/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exchangeapp/exchanger_form.html')
    
    def test_exchange_url_with_right_params(self):
        resp = self.client.get('/exchange/?from=kzt&to=bob&amount=20')
        self.assertEqual(resp.status_code, 200)
        res = ExchangeTest.exch.exchange('kzt', 'bob', 20)
        self.assertEqual(resp.context['exchange_result'], round(res, 3))

    def test_exchange_url_with_wrong_currency(self):
        resp = self.client.get('/exchange/?from=48239&to=not_bob&amount=20')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['from'].lower(), 'eur')
        self.assertEqual(resp.context['to'].lower(), 'kzt')

    def test_exchange_url_with_non_numeric_amount(self):
        resp = self.client.get('/exchange/?from=bob&to=eur&amount=not_amount_34')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['amt'], 1)

    def test_exchange_url_with_negative_amount(self):
        resp = self.client.get('/exchange/?from=bob&to=eur&amount=-34')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['amt'], 34)
        res = ExchangeTest.exch.exchange('bob', 'eur', 34)
        self.assertEqual(resp.context['exchange_result'], round(res, 3))

    def test_exchange_url_with_all_wrong(self):
        resp = self.client.get('/exchange/?from=nevercode\'&to=is4839&amount=cool_very_much')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['from'].lower(), 'eur')
        self.assertEqual(resp.context['to'].lower(), 'kzt')
        self.assertEqual(resp.context['amt'], 1)

class HistoryTest(TestCase):

    def test_history_url_exists(self):
        resp = self.client.get('/history/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exchangeapp/history.html')

    def test_history_url_returns_two_week_stats(self):
        resp = self.client.get('/history/?from=kzt&to=bob')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['changes']), 14)

    def test_history_url_is_two_week_data(self):
        resp = self.client.get('/history/?from=kzt&to=bob')
        self.assertEqual(resp.status_code, 200)
        changes = resp.context['changes']
        for i, date in enumerate(changes):
            arrow_obj = arrow.now().shift(days=-(i+1))
            self.assertEqual(date, arrow_obj.format('MMM DD, YYYY'))

    def test_history_url_with_right_params(self):
        resp = self.client.get('/history/?from=kzt&to=bob')
        self.assertEqual(resp.status_code, 200)

    def test_history_url_with_wrong_params(self):
        resp = self.client.get('/history/?from=see_u&to=today@nevercode')
        self.assertEqual(resp.status_code, 200)

