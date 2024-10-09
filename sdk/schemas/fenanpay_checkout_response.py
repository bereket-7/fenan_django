from schemas.payment_method_type import PaymentMethodTypeDto
from schemas.currency import Currency
from decimal import Decimal
from typing import List, Set, Optional
import json
from dataclasses import dataclass

from sdk.schemas.checkout_split_payment_dto import CheckoutSplitPaymentDto
from sdk.schemas.payment_item import PaymentItem


@dataclass
class FenanpayCheckoutResponse:
    preparePaymentUrl: str


@dataclass
class CheckoutResponseDto:
    callback_url: str
    return_url: str
    unique_id: str
    uuid: str
    company_name: str
    total_amount: float
    currency: Currency
    commission: float
    checkout_beneficiaries: List[CheckoutSplitPaymentDto]
    product_items: List[PaymentItem]
    payment_method_types: Set[PaymentMethodTypeDto]

    def to_dict(self) -> dict:
        return {
            "callbackUrl": self.callback_url,
            "returnUrl": self.return_url,
            "paymentIntentUniqueId": self.unique_id,
            "uuid": self.uuid,
            "companyName": self.company_name,
            "totalAmount": str(self.total_amount),
            "currency": self.currency.value,
            "commission": str(self.commission),
            "checkoutBeneficiaries": [beneficiary.to_dict() for beneficiary in self.checkout_beneficiaries],
            "checkoutItems": [item.to_dict() for item in self.product_items],
            "paymentMethodTypes": [method_type.value for method_type in self.payment_method_types]
        }

    @staticmethod
    def from_dict(data: dict) -> 'CheckoutResponseDto':
        return CheckoutResponseDto(
            callback_url=data.get("callbackUrl", ""),
            return_url=data.get("returnUrl", ""),
            unique_id=data.get("paymentIntentUniqueId", ""),
            uuid=data.get("uuid", ""),
            company_name=data.get("companyName", ""),
            total_amount=Decimal(data.get("totalAmount", "0")),
            currency=Currency(data.get("currency", "")),
            commission=Decimal(data.get("commission", "0")),
            checkout_beneficiaries=[CheckoutSplitPaymentDto.from_dict(
                beneficiary) for beneficiary in data.get("checkoutBeneficiaries", [])],
            product_items=[PaymentItem.from_dict(
                item) for item in data.get("checkoutItems", [])],
            payment_method_types={PaymentMethodTypeDto(
                method) for method in data.get("paymentMethodTypes", [])}
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'CheckoutResponseDto':
        data = json.loads(json_str)
        return CheckoutResponseDto.from_dict(data)
