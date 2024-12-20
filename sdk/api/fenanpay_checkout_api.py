from requests import post, get
from requests.exceptions import RequestException, ConnectionError as RequestsConnectionError
from fenanpay import Fenanpay

from helper.fenanpay_support import FenanpaySupport
from exception.fenanpay_network_exception import FenanpayNetworkException
from schemas.fenanpay_api_response import FenanpayAPIResponse
from schemas.fenanpay_checkout_request import FenanpayCheckoutRequest
from schemas.fenanpay_checkout_session import FenanpayCheckoutSession
from schemas.fenanpay_options import FenanpayOptions


class FenanpayCheckout:
    def __init__(self, http_client):
        self.http_client = http_client

    def create(self, fenanpay_checkout_request: FenanpayCheckoutRequest, option: FenanpayOptions = None):
        if option is None:
            option = FenanpayOptions(sandbox=False)

        try:
            base_path = '/sandbox' if option.sandbox else ''
            endpoint = f"/payment{base_path}/intent"
            response = self.http_client.make_request(
                "POST", endpoint, fenanpay_checkout_request.to_json()
            )
            api_response = FenanpayAPIResponse.to_json(response)
            return api_response
        except RequestsConnectionError as e:
            raise FenanpayNetworkException() from e
        except RequestException as e:
            FenanpaySupport.handle_exception(e)
            raise

    def fetch(self, payment_intent_id: str, option: FenanpayOptions = None) -> FenanpayCheckoutSession:
        if option is None:
            option = FenanpayOptions(sandbox=False)

        try:
            base_path = '/sandbox' if option.sandbox else ''
            endpoint = f"/payment/{base_path}/checkout/{payment_intent_id}"
            response = Fenanpay._make_request(get, endpoint)
            api_response = FenanpayAPIResponse.to_json(response)
            return api_response
        except RequestsConnectionError as e:
            raise FenanpayNetworkException() from e
        except RequestException as e:
            FenanpaySupport.handle_exception(e)
            raise

    def cancel(self, session_id: str, option: FenanpayOptions = None) -> FenanpayCheckoutSession:
        if option is None:
            option = FenanpayOptions(sandbox=False)

        try:
            base_path = '/sandbox' if option.sandbox else ''
            endpoint = f"/payment/{base_path}/intent/cancel/{session_id}"
            response = Fenanpay._make_request(post, endpoint)
            api_response = FenanpayAPIResponse.to_json(response)
            return api_response
        except RequestsConnectionError as e:
            raise FenanpayNetworkException() from e
        except RequestException as e:
            FenanpaySupport.handle_exception(e)
            raise
