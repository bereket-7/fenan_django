import json
from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class PaymentItem:
    name: str
    description: Optional[str]
    image: Optional[str]
    quantity: int
    price: float

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'quantity': self.quantity,
            'price': self.price
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'PaymentItem':
        return PaymentItem(
            name=data.get('name', ''),
            description=data.get('description'),
            image=data.get('image'),
            quantity=data.get('quantity', 0),
            price=data.get('price', 0.0)
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'PaymentItem':
        data = json.loads(json_str)
        return PaymentItem.from_dict(data)
