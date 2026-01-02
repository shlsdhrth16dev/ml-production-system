from typing import Optional
from pydantic import BaseModel, Field


class RawRecord(BaseModel):
    id: int = Field(..., description="Unique record identifier")
    age: int = Field(..., ge=0, le=120)
    income: float = Field(..., ge=0)
    loan_amount: float = Field(..., ge=0)
    defaulted: Optional[int] = Field(None, description="Target variable")
