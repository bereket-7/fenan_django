import json
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
from schemas.payment_item import PaymentItem
from schemas.customer_info import CustomerInfo
from schemas.currency import Currency
from schemas.payment_method_type import PaymentMethodType
from schemas.split_payment import SplitPayment


@dataclass
class FenanpayCheckoutRequest:
    amount: float
    currency: Currency
    payment_intent_unique_id: str
    payment_type: PaymentMethodType
    return_url: str
    expire_in: int
    commission_paid_by_customer: bool

    items: Optional[List[PaymentItem]] = None
    payment_link_unique_id: Optional[str] = None
    split_payment: Optional[SplitPayment] = None
    callback_url: Optional[str] = None
    customer_info: Optional[CustomerInfo] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "amount": self.amount,
            "paymentItem": [item.to_dict() for item in self.items] if self.items else None,
            "currency": self.currency.value,
            "paymentIntentUniqueId": self.payment_intent_unique_id,
            "paymentType": self.payment_type.value,
            "paymentLinkUniqueId": self.payment_link_unique_id,
            "splitPayment": self.split_payment.to_dict() if self.split_payment else None,
            "returnUrl": self.return_url,
            "expireIn": self.expire_in,
            "callbackUrl": self.callback_url,
            "commissionPaidByCustomer": self.commission_paid_by_customer,
            "customerInfo": self.customer_info.to_dict() if self.customer_info else None,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'FenanpayCheckoutRequest':
        return FenanpayCheckoutRequest(
            amount=data.get("amount", 0.0),
            items=[PaymentItem.from_dict(item)
                   for item in data.get("paymentItem", [])] if data.get("paymentItem") else None,
            currency=Currency(data.get("currency", "")),
            payment_intent_unique_id=data.get("paymentIntentUniqueId", ""),
            payment_type=PaymentMethodType(data.get("paymentType", "")),
            payment_link_unique_id=data.get("paymentLinkUniqueId"),
            split_payment=SplitPayment.from_dict(
                data.get("splitPayment")) if data.get("splitPayment") else None,
            return_url=data.get("returnUrl", ""),
            expire_in=data.get("expireIn", 0),
            callback_url=data.get("callbackUrl"),
            commission_paid_by_customer=data.get(
                "commissionPaidByCustomer", False),
            customer_info=CustomerInfo.from_dict(
                data.get("customerInfo")) if data.get("customerInfo") else None,
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'FenanpayCheckoutRequest':
        data = json.loads(json_str)
        return FenanpayCheckoutRequest.from_dict(data)
