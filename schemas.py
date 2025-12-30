from pydantic import BaseModel, Field

class InvestmentInput(BaseModel):
    monthly_investment: float = Field(gt=0)
    annual_increment: float = Field(ge=0)
    equity_pct: float = Field(ge=0, le=1)
    debt_pct: float = Field(ge=0, le=1)
    gold_pct: float = Field(ge=0, le=1)
    equity_return: float = Field(gt=0)
    debt_return: float = Field(gt=0)
    gold_return: float = Field(gt=0)