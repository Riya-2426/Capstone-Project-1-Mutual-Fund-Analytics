import pandas as pd

fund_master= pd.read_csv("data/raw/01_fund_master.csv")

print("Unique fund houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique sub-categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Grades:")
print(fund_master["risk_category"].unique)