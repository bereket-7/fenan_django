from enum import Enum


class TransactionStatus(Enum):
    PENDING = 'PENDING'
    COMPLETED = 'completed'
    FAILED = 'failed'
    CANCELLED = 'cancelled'
