import json
import urllib.request
import arrow

class Exchanger(object):
    API_KEY = "5bbcf670863e47e0ad12322e96022cd1"

    def get_live_currency(self):
        print("Fetching currency data")
        self.currency_live = Exchanger.get_dict_from_json("http://apilayer.net/api/live?access_key=" + Exchanger.API_KEY)
        self.usd_eur = float(self.currency_live["quotes"]["USDEUR"])
        self.usd_kzt = float(self.currency_live["quotes"]["USDKZT"])
        self.usd_bob = float(self.currency_live["quotes"]["USDBOB"])

    def exchange(self, from_curr, to_curr, amount):
        to_usd = float(self.currency_live["quotes"]["USD"+from_curr.upper()])
        from_usd = float(self.currency_live["quotes"]["USD"+to_curr.upper()])
        result = (amount/to_usd)*from_usd
        return round(result, 2)

    def get_two_week_history(self):
        print("Getting two week history")
        two_week_history = {}
        for i in range(1, 15):
            arrow_obj = arrow.now().shift(days=-i)
            currency_stats = Exchanger.get_dict_from_json(
                "http://apilayer.net/api/historical?access_key=" + Exchanger.API_KEY + "&date=" + arrow_obj.format('YYYY-MM-DD'))
            two_week_history[arrow_obj.format('MMM DD, YYYY')] = currency_stats
        self.two_week_history = two_week_history

    @staticmethod
    def get_dict_from_json(url):
        # file = urllib.request.urlopen(url)
        # data = json.loads(file.read().decode())
        with open('mock.json', 'r') as mock_data: 
            print("_MOCKING_")
            data = json.loads(mock_data.read())
        return data

