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

# Load the green trip data from parquet file
green_trips = pd.read_parquet(f'dataset/green_tripdata_{year}-{month:02d}.parquet')
print(f"Dataset shape: {green_trips.shape}")
print(green_trips.head())

trip_zones = pd.read_csv('dataset/taxi_zone_lookup.csv')
print(f"Trip zones shape: {trip_zones.shape}")
print(trip_zones.head())

engine = create_engine('postgresql://root:root@localhost:5433/ny_taxi')

print(pd.io.sql.get_schema(green_trips, name=target_table_greentrip, con=engine))
print(pd.io.sql.get_schema(trip_zones, name=target_table_taxi_zone, con=engine))

green_trips.to_sql(name=target_table_greentrip, con=engine, if_exists='replace')
trip_zones.to_sql(name=target_table_taxi_zone, con=engine, if_exists='replace')

mileorless_distance_trips = green_trips[
    (green_trips['trip_distance'] <= 1)
    & (green_trips['lpep_pickup_datetime'] >= '2025-11-01')
    & (green_trips['lpep_pickup_datetime'] < '2025-12-01')
]

print(f"Mile or less distance trips shape: {mileorless_distance_trips.shape}")