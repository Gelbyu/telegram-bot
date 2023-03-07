import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self, base_url="https://www.google.com/search?q="):
        self.base_url = base_url

    def get_currency_rate(self, currency):
        url = self.base_url + currency + "+to+rub"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        raw_currency_rate = soup.find('div', class_='BNeawe iBp4i AP7Wnd').get_text().split('\n')
        rate = float(raw_currency_rate[1])
        return rate

    def convert_currency(self, currency, amount):
        rate = self.get_currency_rate(currency)
        converted_amount = round(amount * rate, 2)
        return converted_amount