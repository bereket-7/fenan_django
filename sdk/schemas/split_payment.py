import json
from dataclasses import dataclass
from typing import Any, Dict

from schemas.split_type import SplitType


@dataclass
class SplitPayment:
    amount: float
    bank: str
    split_type: SplitType
    credit_account: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "amount": self.amount,
            "bank": self.bank,
            "splitType": self.split_type.value,
            "creditAccount": self.credit_account,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'SplitPayment':
        return SplitPayment(
            amount=data.get("amount", 0.0),
            bank=data.get("bank", ""),
            split_type=data.get("splitType", ""),
            credit_account=data.get("creditAccount", "")
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'SplitPayment':
        data = json.loads(json_str)
        return SplitPayment.from_dict(data)
