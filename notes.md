## Docker Compose
### Connecting to postgres from pgadmin
- since, **pgadmin** and **postgres** both are in the **same docker-compose file**, both containers **share the same network**
- hence, **pgadmin** can connect to postgres using service name i.e. `db`
- **pgadmin** must use the internal post i.e. `5432`


### Connecting to Postgres inside docker-compose from external container
- since, **juashyam:taxi-ingest-v001** docker image is not in the docker-compose, **it does not share the same network as pgadmin**
- hence, **juashyam:taxi-ingest-v001** must connect to docker-compose network i.e. `pipeline_default` in this case
- **juashyam:taxi-ingest-v001** is an external container, so it must use the container name to connect to postgres i.e. `pgdatabse`.
- Though, **juashyam:taxi-ingest-v001** can use `db` also as it is on the same network now as docker-compose
```bash
docker run -it --rm \
  --network=pipeline_default \
  juashyam:taxi-ingest-v001 \
  --pg-host=pgdatabase \
  --pg-port=5432 \
  --month=1 \
  --target-table=yellow_taxi_trips_2021_01
```
```bash
docker run -it --rm \
  --network=pipeline_default \
  juashyam:taxi-ingest-v001 \
  --pg-host=db \
  --pg-port=5432 \
  --month=1 \
  --target-table=yellow_taxi_trips_2021_01
```