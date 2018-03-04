
class Currencies():
    
    currencies = ['eur', 'kzt', 'bob', 'rub']

    def as_choices(self):
        return [(curr, curr.upper()) for curr in Currencies.currencies]

    def as_list(self):
        return Currencies.currencies