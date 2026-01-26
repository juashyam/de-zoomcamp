import pandas as pd
from sqlalchemy import create_engine

pg_user = 'root'
pg_pw = 'root'
pg_host = 'localhost'
pg_port = '5433'
pg_db = 'ny_taxi'
chunksize = 100000
year = 2025
month = 11

target_table_greentrip = f"green_tripdata_{year}_{month:02d}"
target_table_taxi_zone = "taxi_zone_lookup"

# Load the green trip data from downloaded parquet file
green_trips = pd.read_parquet(f'dataset/green_tripdata_{year}-{month:02d}.parquet')
print(f"Dataset shape: {green_trips.shape}")
print(green_trips.head())

# Load the taxi zone lookup data from downloaded CSV file
trip_zones = pd.read_csv('dataset/taxi_zone_lookup.csv')
print(f"Trip zones shape: {trip_zones.shape}")
print(trip_zones.head())

# Create a SQLAlchemy engine to connect to the PostgreSQL database
engine = create_engine('postgresql://root:root@localhost:5433/ny_taxi')

# Print the SQL schema for both dataframes
print(pd.io.sql.get_schema(green_trips, name=target_table_greentrip, con=engine))
print(pd.io.sql.get_schema(trip_zones, name=target_table_taxi_zone, con=engine))

# Write the dataframes to the PostgreSQL database
green_trips.to_sql(name=target_table_greentrip, con=engine, if_exists='replace')
trip_zones.to_sql(name=target_table_taxi_zone, con=engine, if_exists='replace')