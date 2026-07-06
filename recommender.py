import pandas as pd

scheme_performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

sharpe_ranking = pd.read_csv("sharpe_ratio_ranking.csv")

funds = sharpe_ranking.merge(
    scheme_performance[["amfi_code", "risk_grade"]],
    on="amfi_code",
    how="left"
)

risk = input("Enter Risk Appetite (Low / Moderate / High): ").strip().title()

risk_mapping = {
    "Low": ["Low"],
    "Moderate": ["Moderate", "Moderately High"],
    "High": ["High", "Very High"]
}

recommendations = (
    funds[funds["risk_grade"].isin(risk_mapping[risk])]
    .sort_values("Sharpe Ratio", ascending=False)
    .head(3)
)

recommendations = recommendations[
    ["Rank", "scheme_name", "risk_grade", "Sharpe Ratio"]
]
print(f"\nTop 3 Recommended Funds for {risk} Risk Appetite\n")
print(recommendations)