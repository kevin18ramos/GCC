import psycopg2
from psycopg2 import OperationalError
from psycopg2 import pool
import argparse





def connection(USER,PASSWORD,db_to_use,host):
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



