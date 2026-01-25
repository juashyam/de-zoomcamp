import sys
import pandas as pd

print("arguments", sys.argv)

try:
    month = int(sys.argv[1])
    print(f"Running pipeline for month: {month}")
except IndexError:
    print("month is not provided as argument!!!")
    sys.exit()

df = pd.DataFrame({'day': [1, 2], 'num_passengers': [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet")

