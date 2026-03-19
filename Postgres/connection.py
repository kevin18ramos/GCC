from psycopg2 import pool
import argparse
import task as t
import psycopg2
from psycopg2 import OperationalError
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR.parent / "gc.config" / "host_file.txt"

def connection(file_path):
    conn_info = t.read_host_file(file_path)
    try:
        conn = psycopg2.connect(
            host=conn_info['host'],
            database=conn_info['db_to_use'],
            user=conn_info['user'],
            password=conn_info['password']
        )

        cursor = conn.cursor()

        return conn, cursor

    except OperationalError as e:
        print("Connection failed")
        print(e)
        exit(0)


def pool_connection(USER,PASSWORD,db_to_use,host):
    try:

        db_pool = pool.SimpleConnectionPool(
            1, 4,
            host=host,
            database=db_to_use,
            user=USER,
            password=PASSWORD
        )

        # Get connection from pool
        connection = db_pool.getconn()

        # Create cursor
        cursor = connection.cursor()

        return cursor

    except OperationalError as e:
        print("Connection failed")
        print(e)
        exit(0)



