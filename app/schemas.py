from typing import List
import uuid
from pydantic import BaseModel

class PayloadCreate(BaseModel):
    list_1: List[str]
    list_2: List[str]

class PayloadRead(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    output: str