import json
import requests
from datetime import datetime
import logging

from exception.fenanpay_bad_request_exception import FenanpayBadRequestException
from exception.fenanpay_exception import FenanpayException
from exception.fenanpay_network_exception import FenanpayNetworkException
from exception.fenanpay_not_found_exception import FenanpayNotFoundException
from exception.fenanpay_unauthorized_exception import FenanpayUnauthorizedException

# Set up logging
logger = logging.getLogger(__name__)


class FenanpaySupport:
    @staticmethod
    def get_expire_date_from_date(date: datetime) -> str:
        return date.strftime('%Y-%m-%dT%H:%M:%S')

    @staticmethod
    def handle_exception(e: requests.exceptions.RequestException):
        if isinstance(e, requests.exceptions.HTTPError):
            response = e.response
            if response:
                status_code = response.status_code
                response_body = response.text

                if status_code == 401:
                    logger.error('Invalid authentication credentials')
                    raise FenanpayUnauthorizedException(
                        'Invalid authentication credentials') from e
                elif status_code == 400:
                    try:
                        response_json = response.json()
                        msg = response_json.get(
                            'msg', 'Invalid Request, check your Request body.')
                    except json.JSONDecodeError:
                        msg = 'Invalid Request, check your Request body.'
                    logger.error(msg)
                    raise FenanpayBadRequestException(msg) from e
                elif status_code == 404:
                    try:
                        response_json = response.json()
                        msg = response_json.get(
                            'msg', 'Invalid Request, Not found.')
                    except json.JSONDecodeError:
                        msg = 'Invalid Request, Not found.'
                    logger.error(msg)
                    raise FenanpayNotFoundException(msg) from e
                else:
                    try:
                        response_json = response.json()
                        msg = response_json.get('msg', 'An error occurred.')
                    except json.JSONDecodeError:
                        msg = 'An error occurred.'
                    logger.error(msg)
                    raise FenanpayException(msg) from e
        else:
            logger.error('A network error occurred')
            raise FenanpayNetworkException('A network error occurred') from e
