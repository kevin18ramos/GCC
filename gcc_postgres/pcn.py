from psycopg2 import pool
import argparse
from . import task as t
import psycopg2
from psycopg2 import OperationalError
from pathlib import Path


def d_cn(caller_file):
    #direct connection
    base_dir = Path(caller_file).resolve().parent
    file_path = base_dir.parent / "gc.config" / "host_file.txt"
    conn_info = read_host_file(file_path)

    try:
        conn = psycopg2.connect(
            host=conn_info['host'],
            database=conn_info['db_name'],
            user=conn_info['user'],
            password=conn_info['password']
        )

        cursor = conn.cursor()

        return conn, cursor

    except OperationalError as e:
        print("Connection failed")
        print(e)
        return e


def pool(caller_file):
    #direct connection
    base_dir = Path(caller_file).resolve().parent
    file_path = base_dir.parent / "gc.config" / "host_file.txt"
    conn_info = read_host_file(file_path)
    try:

        db_pool = pool.SimpleConnectionPool(
            1, 4,
            host=conn_info['host'],
            database=conn_info['db_name'],
            user=conn_info['user'],
            password=conn_info['password']
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


def read_host_file(file_path):
    with open(file_path, "r") as f:
        line = f.readline().strip()

    parts = [p.strip() for p in line.split("|")]

    if len(parts) != 4:
        raise ValueError("Invalid host file format")

    db_name, host, user, password = parts

    return {
        "db_name": db_name,
        "host": host,
        "user": user,
        "password": password
    }
