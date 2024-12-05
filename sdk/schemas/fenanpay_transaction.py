import json
from dataclasses import dataclass
from typing import Dict, Any

from schemas.payment_method_type import PaymentMethodType
from schemas.transaction_status import TransactionStatus


@dataclass
class FenanpayTransaction:
    id: str
    transaction_id: str
    payment_type: PaymentMethodType
    transaction_status: TransactionStatus
    created_at: str
    updated_at: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "transactionId": self.transaction_id,
            "paymentType": self.payment_type.value,
            "transactionStatus": self.transaction_status.value,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'FenanpayTransaction':
        return FenanpayTransaction(
            id=data["id"],
            transaction_id=data["transactionId"],
            payment_type=PaymentMethodType(data["paymentType"]),
            transaction_status=TransactionStatus(data["transactionStatus"]),
            created_at=data["createdAt"],
            updated_at=data["updatedAt"]
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'FenanpayTransaction':
        data = json.loads(json_str)
        return FenanpayTransaction.from_dict(data)
