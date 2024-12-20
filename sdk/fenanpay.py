import requests


class Fenanpay:
    DEFAULT_HOST = 'https://api.fenanpay.com/api'
    API_VERSION = '/v1'
    PACKAGE_VERSION = '1.0.0'
    DEFAULT_TIMEOUT = 120

    def __init__(self, apikey):
        self.apikey = apikey
        self.headers = {
            'apiKey': self.apikey,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        from api.fenanpay_checkout_api import FenanpayCheckout
        from api.direct_pay_api import DirectPay
        self.checkout = FenanpayCheckout(self)
        self.direct_pay = DirectPay(self)

    def make_request(self, method, endpoint, data=None):
        url = f"{Fenanpay.DEFAULT_HOST}{Fenanpay.API_VERSION}{endpoint}"
        print(f"Requesting URL: {url}")
        response = requests.request(
            method, url, headers=self.headers, json=data, timeout=Fenanpay.DEFAULT_TIMEOUT)
        response.raise_for_status()
        return response.json()
