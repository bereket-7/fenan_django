import json
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

from customer_info import CustomerInfo
from sdk.schemas.currency import Currency
from sdk.schemas.payment_method_type import PaymentMethodType
from split_payment import SplitPayment


@dataclass
class PaymentIntent:
    amount: float
    items: List[Dict[str, Any]]
    currency: Currency
    payment_intent_unique_id: str
    payment_link_unique_id: str
    method_type: List[PaymentMethodType]
    split_payment: List[SplitPayment]
    return_url: str
    expire_in: int
    callback_url: str
    commission_paid_by_customer: bool
    customer_info: Optional[CustomerInfo]

    def to_dict(self) -> Dict[str, Any]:
        return {
            'amount': self.amount,
            'items': self.items,
            'currency': self.currency,
            'paymentIntentUniqueId': self.payment_intent_unique_id,
            'paymentLinkUniqueId': self.payment_link_unique_id,
            'methodType': [method.value for method in self.method_type],
            'splitPayment': [sp.to_dict() for sp in self.split_payment],
            'returnUrl': self.return_url,
            'expireIn': self.expire_in,
            'callbackUrl': self.callback_url,
            'commissionPaidByCustomer': self.commission_paid_by_customer,
            'customerInfo': self.customer_info.to_dict() if self.customer_info else None,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'PaymentIntent':
        return PaymentIntent(
            amount=data.get('amount', 0.0),
            items=data.get('items', []),
            currency=data.get('currency', ''),
            payment_intent_unique_id=data.get('paymentIntentUniqueId', ''),
            payment_link_unique_id=data.get('paymentLinkUniqueId', ''),
            method_type=[PaymentMethodType(m)
                         for m in data.get('methodType', [])],
            split_payment=[SplitPayment.from_dict(
                sp) for sp in data.get('splitPayment', [])],
            return_url=data.get('returnUrl', ''),
            expire_in=data.get('expireIn', 0),
            callback_url=data.get('callbackUrl', ''),
            commission_paid_by_customer=data.get(
                'commissionPaidByCustomer', 0.0),
            customer_info=CustomerInfo.from_dict(
                data['customerInfo']) if 'customerInfo' in data else None
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'PaymentIntent':
        data = json.loads(json_str)
        return PaymentIntent.from_dict(data)
