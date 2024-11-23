import json
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from sdk.schemas.currency import Currency
from sdk.schemas.customer_info import CustomerInfo
from sdk.schemas.payment_item import PaymentItem
from sdk.schemas.payment_method_type import PaymentMethodType
from sdk.schemas.split_payment import SplitPayment


@dataclass
class FenanpayCheckoutRequest:
    amount: float
    items: List[PaymentItem]
    currency: Currency
    payment_intent_unique_id: str
    payment_type: PaymentMethodType
    payment_link_unique_id: Optional[str]
    split_payment: Optional[SplitPayment]
    return_url: str
    expire_in: int
    callback_url: Optional[str]
    commission_paid_by_customer: bool
    customer_info: Optional[CustomerInfo]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "amount": self.amount,
            "paymentItem": [item.to_dict() for item in self.items],
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
                   for item in data.get("items", [])],
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
