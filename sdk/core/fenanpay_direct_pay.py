from direct_pay.direct_pay import DirectPay
from schemas.payment_method_type import PaymentMethodType


class FenanpayDirectPay:
    def __init__(self, http_client):
        self.http_client = http_client
        self.telebirr = DirectPay(
            PaymentMethodType.TELE_BIRR, self.http_client)
        self.cbe = DirectPay(PaymentMethodType.CBE, self.http_client)
        self.etswitch = DirectPay(
            PaymentMethodType.ETS_SWITCH, self.http_client)
