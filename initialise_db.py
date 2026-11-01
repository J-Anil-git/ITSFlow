"""Create the ITS Flow database and its tables.

Usage:  python initialise_db.py

1. Connects to the default "postgres" database and creates the itsflow
   database if it does not exist yet.
2. Connects to itsflow and runs sql/create_tables.sql, which drops and
   re-creates the department, it_user and ticket tables.
"""
from pathlib import Path

import psycopg2
from psycopg2 import sql

from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

SCHEMA_FILE = Path(__file__).parent / "sql" / "create_tables.sql"


def connect(dbname):
    return psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=dbname,
                            user=DB_USER, password=DB_PASSWORD)


def create_database():
    conn = connect("postgres")
    conn.autocommit = True  # CREATE DATABASE cannot run inside a transaction
    with conn.cursor() as cur:
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
        if cur.fetchone():
            print(f"Database '{DB_NAME}' already exists.")
        else:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
            print(f"Created database '{DB_NAME}'.")
    conn.close()


def create_tables():
    conn = connect(DB_NAME)
    with conn, conn.cursor() as cur:
        cur.execute(SCHEMA_FILE.read_text())
    conn.close()
    print("Created tables: department, it_user, ticket.")


if __name__ == "__main__":
    create_database()
    create_tables()
