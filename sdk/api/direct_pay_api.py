from helper.fenanpay_support import FenanpaySupport
from schemas.fenanpay_api_response import FenanpayAPIResponse
from exception.fenanpay_network_exception import FenanpayNetworkException
from schemas.payment_intent import PaymentIntent
from requests.exceptions import RequestException, ConnectionError


class DirectPay:
    def __init__(self, http_client):
        self.http_client = http_client

    def pay(self, payment_intent: PaymentIntent):
        try:
            endpoint = f"/payment/express/pay"
            response = self.http_client.make_request(
                "POST", endpoint, payment_intent.to_json())
            api_response = FenanpayAPIResponse.to_json(response)
            return api_response
        except ConnectionError as e:
            raise FenanpayNetworkException() from e
        except RequestException as e:
            FenanpaySupport.handle_exception(e)
            raise e
