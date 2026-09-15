import hashlib
import json
from datetime import datetime, timezone
from typing import TypeVar

T = TypeVar("T")


class Block:
    def __init__(
        self,
        index: int,
        data: dict[str, T],
        previous_hash: str
    ):
        self.index = index
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }

        encoded = json.dumps(
            block_data,
            sort_keys=True
        ).encode()

        return hashlib.sha256(encoded).hexdigest()
