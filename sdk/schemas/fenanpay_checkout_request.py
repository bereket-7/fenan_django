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
    payment_item: List[PaymentItem]
    currency: Currency
    paymentIntentUniqueId: str
    payment_type: PaymentMethodType
    paymentLinkUniqueId: Optional[str]
    splitPayment: Optional[SplitPayment]
    returnUrl: str
    expireIn: int
    callbackUrl: Optional[str]
    commissionPaidByCustomer: bool
    customerInfo: Optional[CustomerInfo]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "amount": self.amount,
            "paymentItem": [item.to_dict() for item in self.payment_item],
            "currency": self.currency.value,
            "paymentIntentUniqueId": self.paymentIntentUniqueId,
            "paymentType": self.payment_type.value,
            "paymentLinkUniqueId": self.paymentLinkUniqueId,
            "splitPayment": self.splitPayment.to_dict() if self.splitPayment else None,
            "returnUrl": self.returnUrl,
            "expireIn": self.expireIn,
            "callbackUrl": self.callbackUrl,
            "commissionPaidByCustomer": self.commissionPaidByCustomer,
            "customerInfo": self.customerInfo.to_dict() if self.customerInfo else None,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'FenanpayCheckoutRequest':
        return FenanpayCheckoutRequest(
            amount=data.get("amount", 0.0),
            payment_item=[PaymentItem.from_dict(
                item) for item in data.get("paymentItem", [])],
            currency=Currency(data.get("currency", "")),
            paymentIntentUniqueId=data.get("paymentIntentUniqueId", ""),
            payment_type=PaymentMethodType(data.get("paymentType", "")),
            paymentLinkUniqueId=data.get("paymentLinkUniqueId"),
            splitPayment=SplitPayment.from_dict(
                data.get("splitPayment")) if data.get("splitPayment") else None,
            returnUrl=data.get("returnUrl", ""),
            expireIn=data.get("expireIn", 0),
            callbackUrl=data.get("callbackUrl"),
            commissionPaidByCustomer=data.get(
                "commissionPaidByCustomer", False),
            customerInfo=CustomerInfo.from_dict(
                data.get("customerInfo")) if data.get("customerInfo") else None,
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'FenanpayCheckoutRequest':
        data = json.loads(json_str)
        return FenanpayCheckoutRequest.from_dict(data)
