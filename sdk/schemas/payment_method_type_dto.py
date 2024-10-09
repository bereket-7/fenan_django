from dataclasses import dataclass
from typing import Optional

from schemas.payment_method_type import PaymentMethodType
from schemas.currency import Currency


@dataclass
class PaymentMethodTypeDto:
    payment_type_id: Optional[int]
    name: str
    description: str
    type: str
    options: Optional[str]
    enabled: bool
    currency: Optional[Currency]
    code: Optional[PaymentMethodType]
