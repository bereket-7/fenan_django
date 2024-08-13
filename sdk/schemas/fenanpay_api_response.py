import json
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class FenanpayAPIResponse:
    status: Any
    message: Any
    content: Any

    def to_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'message': self.message,
            'content': self.content,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'FenanpayAPIResponse':
        return FenanpayAPIResponse(
            status=data['status'],
            message=data['message'],
            content=data['content']
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'FenanpayAPIResponse':
        data = json.loads(json_str)
        return FenanpayAPIResponse.from_dict(data)
