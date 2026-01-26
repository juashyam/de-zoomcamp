import sys
import pandas as pd
import os

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

# Show file stats
print(f"\nParquet file stats:")
file_path = f"output_{month}.parquet"
file_size = os.path.getsize(file_path)
print(f"Size: {file_size} bytes ({file_size / 1024:.2f} KB)")
print(f"Exists: {os.path.exists(file_path)}")

# Read back and show DataFrame info
df_read = pd.read_parquet(file_path)
print(f"Rows: {len(df_read)}")
print(f"Columns: {list(df_read.columns)}")
print("Pipeline execution completed.")