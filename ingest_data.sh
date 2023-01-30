#!/bin/bash

#URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2019-01.parquet"

docker run -it \
   --network=pg-network \
   taxi_ingest:v001 \
   --user=root \
   --password=root \
   --host=pg-database \
   --port=5432 \
   --db=ny_taxi \
   --table_name=yellow_taxi_data \
   --url=${URL}
