# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .PaymentRequestMemo import PaymentRequestMemo

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TxAckPaymentRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 37
    UNSTABLE = True

    def __init__(
        self,
        *,
        recipient_name: str,
        amount: int,
        signature: bytes,
        memos: List[PaymentRequestMemo] = None,
        nonce: bytes = None,
    ) -> None:
        self.memos = memos if memos is not None else []
        self.recipient_name = recipient_name
        self.amount = amount
        self.signature = signature
        self.nonce = nonce

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('recipient_name', p.UnicodeType, p.FLAG_REQUIRED),
            2: ('amount', p.UVarintType, p.FLAG_REQUIRED),
            3: ('memos', PaymentRequestMemo, p.FLAG_REPEATED),
            4: ('nonce', p.BytesType, None),
            5: ('signature', p.BytesType, p.FLAG_REQUIRED),
        }
