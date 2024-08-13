from enum import Enum


class TransactionStatus(Enum):
    PROCESSING = 'PROCESSING'
    FAILED = 'FAILED'
    SUCCESS = 'SUCCESS'
    EXPIRED = 'EXPIRED'
