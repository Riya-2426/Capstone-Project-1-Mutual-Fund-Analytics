import requests
import pandas as pd
import os

schemes={
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}
print("="*60)
print("FETCHING LIVE NAV DATA")
print("="*60)

for scheme_name, amfi_code in schemes.items():
    url=f"https://api.mfapi.in/mf/{amfi_code}"

    try:
        response= requests.get(url, timeout=10)
        if response.status_code== 200:
            data= response.json()
            nav_df= pd.DataFrame(data["data"])
            file_path= f"data/raw/{scheme_name}_NAV.csv"
            nav_df.to_csv(file_path, index=False)

            print(f"{scheme_name} data saved successfully")
            print(f" Records: {len(nav_df)}")
            print(f" File: {file_path}\n")
        else:
            print("Failed to fetch {scheme_name}")
            print("Status code: {response.status_code}\n")

    except Exception as e:
        print("Error fetching {scheme_name}")
        print("Error: {e}\n")
        
print("="*60)
print("NAV DATA FETCHING COMPLETED")
print("="*60)
