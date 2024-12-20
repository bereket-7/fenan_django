from dataclasses import dataclass
import json
from typing import List, Dict, Any, Optional
from schemas.customer_info import CustomerInfo
from schemas.currency import Currency
from schemas.payment_method_type import PaymentMethodType
from schemas.split_payment import SplitPayment


@dataclass
class PaymentIntent:
    amount: float
    currency: Currency
    payment_intent_unique_id: str
    method_type: List[PaymentMethodType]
    return_url: str
    expire_in: int
    callback_url: str
    commission_paid_by_customer: bool

    items: Optional[List[Dict[str, Any]]] = None
    payment_link_unique_id: Optional[str] = None
    split_payment: Optional[List[SplitPayment]] = None
    customer_info: Optional[CustomerInfo] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            'amount': self.amount,
            'items': self.items or [],
            'currency': self.currency.value,
            'paymentIntentUniqueId': self.payment_intent_unique_id,
            'paymentLinkUniqueId': self.payment_link_unique_id,
            'methodType': [method.value for method in self.method_type],
            'splitPayment': [sp.to_dict() for sp in self.split_payment] if self.split_payment else [],
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
            currency=Currency(data.get('currency', '')),
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
                'commissionPaidByCustomer', False),
            customer_info=CustomerInfo.from_dict(
                data['customerInfo']) if 'customerInfo' in data else None,
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'PaymentIntent':
        data = json.loads(json_str)
        return PaymentIntent.from_dict(data)
