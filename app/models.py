from sqlmodel import SQLModel, Field, UniqueConstraint
from datetime import datetime
from typing import Optional

class TransformedString(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    original: str = Field(index=True, sa_column_kwargs={"unique": True})
    transformed: str

class Payload(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    output: str = Field(index=True, sa_column_kwargs={"unique": True})
    created_at: datetime = Field(default_factory=datetime.utcnow)

    __table_args__ = (UniqueConstraint("output"), )