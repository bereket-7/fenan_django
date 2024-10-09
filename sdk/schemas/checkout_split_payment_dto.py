from dataclasses import dataclass
from typing import Optional

from sdk.schemas.split_type import SplitType


@dataclass
class CheckoutSplitPaymentDto:
    split_id: int
    account_number: str
    amount: float
    split_type: Optional[SplitType]
