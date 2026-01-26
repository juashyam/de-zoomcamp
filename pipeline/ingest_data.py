import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

# map data types of non-datetime fields
dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

# map data types of datetime fields
parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL username')
@click.option('--pg-pw', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--year', default=2021, help='Year of the data to ingest', type=int)
@click.option('--month', default=1, help='Month of the data to ingest', type=int)
@click.option('--chunksize', default=100000, help='Number of rows per chunk', type=int)
@click.option('--target-table', default='yellow_taxi_data', help='Target table name in PostgreSQL')
def run(pg_user, pg_pw, pg_host, pg_port, pg_db, year, month, chunksize, target_table):
    """
    Ingest NYC taxi data into PostgreSQL database in chunks.

    Example usage:

    python ingest_data.py \
        --pg-user=root \
        --pg-pw=root \
        --pg-host=localhost \
        --pg-port=5432 \
        --pg-db=ny_taxi \
        --year=2021 \
        --month=1 \
        --chunksize=100000 \
        --target-table=yellow_taxi_data_2021_01

    python ingest_data.py \
        --year=2021 \
        --month=1 \
        --target-table=yellow_taxi_data_2021_01

    """

    print(f"Starting data ingestion for {year}-{month:02d} into table '{target_table}'")

    # prepare url to taxi data. currently, official ny taxi data only provides datasets in parquet format.
    # we're downloading the older data from a forked repo by DataTalks Club.
    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow'
    url = f"{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz"

    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize
    )

    # import sqlalchemy to work with postgresql
    engine = create_engine(f'postgresql://{pg_user}:{pg_pw}@{pg_host}:{pg_port}/{pg_db}')

    first = True
    for df_chunk in tqdm(df_iter):
        if first:
            df_chunk.head(0).to_sql(
                name=target_table,
                con=engine,
                if_exists='replace'
            )
            first = False

        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists='append'
        )

if __name__ == "__main__":
    run()