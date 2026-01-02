from pydantic import BaseModel, Field


class LoanRecord(BaseModel):
    # Identifier (validated but not used for modeling)
    LoanID: str

    # Numeric features
    Age: int = Field(..., ge=0, le=120)
    Income: int = Field(..., ge=0)
    LoanAmount: int = Field(..., ge=0)
    CreditScore: int = Field(..., ge=300, le=900)
    MonthsEmployed: int = Field(..., ge=0)
    NumCreditLines: int = Field(..., ge=0)
    InterestRate: float = Field(..., ge=0)
    LoanTerm: int = Field(..., ge=0)
    DTIRatio: float = Field(..., ge=0)

    # Categorical features
    Education: str
    EmploymentType: str
    MaritalStatus: str
    HasMortgage: str
    HasDependents: str
    LoanPurpose: str
    HasCoSigner: str

    # Target
    Default: int = Field(..., ge=0, le=1)
