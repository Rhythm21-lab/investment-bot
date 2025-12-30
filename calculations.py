def calculate_excel_style_corpus(
    monthly_investment,
    allocation_pct,
    annual_increment,
    expected_return,
    years=20
):
    annual_investment = monthly_investment * 12 * allocation_pct
    corpus = 0
    rate = expected_return / 100

    for _ in range(years):
        corpus = (corpus + annual_investment) * (1 + rate)
        annual_investment *= (1 + annual_increment / 100)

    return round(corpus, 2)


def calculate_full_portfolio(data):
    equity = calculate_excel_style_corpus(
        data["monthly_investment"],
        data["equity_pct"],
        data["annual_increment"],
        data["equity_return"]
    )

    debt = calculate_excel_style_corpus(
        data["monthly_investment"],
        data["debt_pct"],
        data["annual_increment"],
        data["debt_return"]
    )

    gold = calculate_excel_style_corpus(
        data["monthly_investment"],
        data["gold_pct"],
        data["annual_increment"],
        data["gold_return"]
    )

    return {
        "equity_corpus": equity,
        "debt_corpus": debt,
        "gold_corpus": gold,
        "total_corpus": round(equity + debt + gold, 2)
    }