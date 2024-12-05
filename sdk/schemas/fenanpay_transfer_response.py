import json
from dataclasses import dataclass
from typing import Optional
from schemas.fenanpay_transaction import FenanpayTransaction


@dataclass
class FenanpayTransferResponse:
    session_id: str
    url: Optional[str]
    otp: Optional[str]
    transaction: Optional[FenanpayTransaction]

    def to_dict(self) -> dict:
        return {
            "sessionId": self.session_id,
            "url": self.url,
            "otp": self.otp,
            "transaction": self.transaction.to_dict() if self.transaction else None,
        }

    @staticmethod
    def from_dict(data: dict) -> 'FenanpayTransferResponse':
        return FenanpayTransferResponse(
            session_id=data.get("sessionId", ""),
            url=data.get("url", ""),
            otp=data.get("otp", ""),
            transaction=FenanpayTransaction.from_dict(
                data["transaction"]) if "transaction" in data else None
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'FenanpayTransferResponse':
        data = json.loads(json_str)
        return FenanpayTransferResponse.from_dict(data)
