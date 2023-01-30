#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import argparse
import os

from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_name = 'output.parquet'

    os.system(f"wget {url} -O {parquet_name}")

    df = pd.read_parquet(parquet_name, engine='pyarrow')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    df.to_sql(name=table_name, con=engine, if_exists='append', chunksize=150000)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest parquet data to Postgres')

    # user, password, host, port, database name, table name, url of the parquet file
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='table name for postgres')
    parser.add_argument('--url', help='url of the parquet file')

    args = parser.parse_args()

    main(args)
