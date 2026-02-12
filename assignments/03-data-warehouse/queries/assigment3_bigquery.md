## Creating external table referring to gcs path
```sql
CREATE OR REPLACE EXTERNAL TABLE `de-zoomcamp-sandbox-487011.zoomcamp.external_assignment3_yellow_tripdata_2024`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de-zoomcamp-sandbox-487011-bucket/yellow_tripdata_2024-*.parquet']
);
```

## Create a non-partitioned table from external table
```sql
CREATE OR REPLACE TABLE de-zoomcamp-sandbox-487011.zoomcamp.assignment3_yellow_tripdata_2024_non_partitioned AS
SELECT * FROM de-zoomcamp-sandbox-487011.zoomcamp.external_assignment3_yellow_tripdata_2024;
```

## Count number of trips from materialized table
```sql
SELECT count(*) as trips
FROM de-zoomcamp-sandbox-487011.zoomcamp.assignment3_yellow_tripdata_2024_non_partitioned;
```

## Count number of unique PULocationID from external table
```sql
SELECT COUNT(DISTINCT(PULocationID)) as unique_pulocation_ids
FROM de-zoomcamp-sandbox-487011.zoomcamp.external_assignment3_yellow_tripdata_2024;
```

## Count number of unique PULocationID from materialized table
```sql
SELECT COUNT(DISTINCT(PULocationID)) as unique_pulocation_ids
FROM de-zoomcamp-sandbox-487011.zoomcamp.assignment3_yellow_tripdata_2024_non_partitioned;
```

## Select single column (PULocationID) from materialized table
```sql
SELECT PULocationID
FROM de-zoomcamp-sandbox-487011.zoomcamp.assignment3_yellow_tripdata_2024_non_partitioned;
```

## Select two columns (PULocationID, DOLocationID) from materialized table
```sql
SELECT PULocationID, DOLocationID
FROM de-zoomcamp-sandbox-487011.zoomcamp.assignment3_yellow_tripdata_2024_non_partitioned;
```

## Count trips with 0 fair amount
```sql
SELECT COUNT(*)
FROM de-zoomcamp-sandbox-487011.zoomcamp.assignment3_yellow_tripdata_2024_non_partitioned
WHERE fare_amount = 0;
```

## Create partitioned and clustered table
```sql
CREATE OR REPLACE TABLE de-zoomcamp-sandbox-487011.zoomcamp.assignment3_yellow_tripdata_2024_partitioned_clustered
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT * FROM de-zoomcamp-sandbox-487011.zoomcamp.assignment3_yellow_tripdata_2024_non_partitioned;
```

## Count unique vendor ids from materialized table between a dropoff date range
```sql
SELECT count(DISTINCT(VendorID)) as total_vendors
FROM de-zoomcamp-sandbox-487011.zoomcamp.assignment3_yellow_tripdata_2024_non_partitioned
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';
```

## Count unique vendor ids from partitioned and clustered table between a dropoff date range

```sql
SELECT count(DISTINCT(VendorID)) as total_vendors
FROM de-zoomcamp-sandbox-487011.zoomcamp.assignment3_yellow_tripdata_2024_partitioned_clustered
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';
```