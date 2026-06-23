import pandas as pd
import os
DATA_PATH= "data/raw"
csv_files= [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print(f"\nTotal CSV files found: {len(csv_files)}")

for file in csv_files:
    print("\n"+ "="*60)
    print(f"FILE: {file}")
    file_path= os.path.join(DATA_PATH, file)

    try:
        df= pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 rows:")
        print(df.head())

        print("\nMissing values:")
        print(df.isnull().sum())
    except Exception as e:
        print(f"Error reading {file}: {e}")
    

