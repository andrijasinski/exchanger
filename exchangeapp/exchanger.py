import json
import urllib.request


class Exchanger(object):
    API_KEY = "5bbcf670863e47e0ad12322e96022cd1"

    def get_live_currency(self):
        print("Fetching currency data")
        self.currency_live = Exchanger.getDictFromJson("http://apilayer.net/api/live?access_key=" + Exchanger.API_KEY)
        self.usd_eur = float(self.currency_live["quotes"]["USDEUR"])
        self.usd_kzt = float(self.currency_live["quotes"]["USDKZT"])
        self.usd_bob = float(self.currency_live["quotes"]["USDBOB"])

    @staticmethod
    def getDictFromJson(url):
        file = urllib.request.urlopen(url)
        data = json.loads(file.read().decode())
        return data

