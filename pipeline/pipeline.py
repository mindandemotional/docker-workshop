import sys
import pandas as pd

print("arguments", sys.argv)

month = int(sys.argv[1])
print(f"Running pipeline for month {month}")

df = pd.DataFrame({"day": [1, 2], "num passengers": [3, 4]})
df['month'] = month
df.to_parquet(f"output_month_{sys.argv[1]}.parquet")

print(df.head())
