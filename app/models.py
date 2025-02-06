from sqlmodel import SQLModel, Field, UniqueConstraint
from datetime import datetime
from typing import Optional

class TransformedString(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    original: str = Field(index=True, sa_column_kwargs={"unique": True})
    transformed: str

