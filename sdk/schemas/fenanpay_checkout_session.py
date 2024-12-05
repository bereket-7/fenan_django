import json
from dataclasses import dataclass
from typing import Optional, Any, Dict

from schemas.fenanpay_transaction import FenanpayTransaction


@dataclass
class FenanpayCheckoutSession:
    id: str
    transaction: Optional[FenanpayTransaction]
    total_amount: float
    test: Optional[bool]
    uuid: str
    created_at: str
    updated_at: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "transaction": self.transaction.to_dict() if self.transaction else None,
            "totalAmount": self.total_amount,
            "test": self.test,
            "uuid": self.uuid,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'FenanpayCheckoutSession':
        # Assume FenanpayTransaction has a `from_dict` method
        transaction = FenanpayTransaction.from_dict(
            data["transaction"]) if data.get("transaction") else None
        return FenanpayCheckoutSession(
            id=data["id"],
            transaction=transaction,
            total_amount=data["totalAmount"],
            test=data.get("test"),
            uuid=data["uuid"],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"]
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'FenanpayCheckoutSession':
        data = json.loads(json_str)
        return FenanpayCheckoutSession.from_dict(data)
