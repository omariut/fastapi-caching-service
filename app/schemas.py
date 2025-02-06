from pydantic import BaseModel, model_validator
from typing import List
from typing_extensions import Self

class PayloadCreate(BaseModel):
    list_1: List[str]
    list_2: List[str]

    @model_validator(mode='after')
    def check_length_match(self) -> Self:
        if len(self.list_1) != len(self.list_2):
            raise ValueError("Lists must be of the same length")
        return self

class PayloadRead(BaseModel):
    id: int
    output: str