from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from schemas import InvestmentInput
from calculations import calculate_full_portfolio

app = FastAPI(
    title="20-Year Investment Corpus Calculator",
    description="Excel-based compounding model for Equity, Debt & Gold",
    version="1.0"
)

@app.post("/calculate")
def calculate_corpus(input: InvestmentInput):

    allocation_sum = (
        input.equity_pct +
        input.debt_pct +
        input.gold_pct
    )

    if round(allocation_sum, 2) != 1:
        raise HTTPException(
            status_code=400,
            detail="Equity + Debt + Gold allocation must sum to 1 (100%)"
        )

    return calculate_full_portfolio(input.dict())

# Serve index.html at "/"
app.mount("/", StaticFiles(directory="static", html=True), name="static")