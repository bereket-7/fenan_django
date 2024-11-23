import requests
from requests.exceptions import RequestException, ConnectionError as RequestsConnectionError
from sdk import fenanpay

from helper.fenanpay_support import FenanpaySupport
from exception.fenanpay_network_exception import FenanpayNetworkException
from schemas.fenanpay_api_response import FenanpayAPIResponse
from schemas.fenanpay_checkout_request import FenanpayCheckoutRequest
from schemas.fenanpay_checkout_response import FenanpayCheckoutResponse
from schemas.fenanpay_checkout_session import FenanpayCheckoutSession
from schemas.fenanpay_options import FenanpayOptions


class FenanpayCheckout:
    def __init__(self, http_client):
        self.http_client = http_client

    def create(self, fenanpay_checkout_request: FenanpayCheckoutRequest, option: FenanpayOptions = None) -> FenanpayCheckoutResponse:
        if option is None:
            option = FenanpayOptions(sandbox=False)

        try:
            base_path = '/sandbox' if option.sandbox else ''
            url = f"{fenanpay.API_VERSION}/payment{base_path}/intent"
            response = self.http_client.post(
                url, json=fenanpay_checkout_request.to_dict())

            arif_api_response = FenanpayAPIResponse.from_json(response.json())
            return arif_api_response.content
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
            url = f"{
                fenanpay.API_VERSION}/payment/{base_path}/checkout/payment_intent_id"
            response = self.http_client.get(url)

            arif_api_response = FenanpayAPIResponse.from_json(response.json())
            return FenanpayCheckoutResponse.from_json(arif_api_response.content)
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
            url = f"{fenanpay.API_VERSION}{
                base_path}/payment/intent/cancel/{session_id}"
            response = self.http_client.post(url)

            arif_api_response = FenanpayAPIResponse.from_json(response.json())
            return FenanpayCheckoutSession.from_json(arif_api_response.content)
        except RequestsConnectionError as e:
            raise FenanpayNetworkException() from e
        except RequestException as e:
            FenanpaySupport.handle_exception(e)
            raise
