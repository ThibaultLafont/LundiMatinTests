import psycopg2
from dotenv import load_dotenv
import os
import time
import psycopg2
from psycopg2 import OperationalError

def create_conn():
    conn = None
    while not conn:
        try:
            conn = psycopg2.connect(
                dbname="lundi_matin",
                user="postgres",
                password="password",
                host="db",
                port="5432",
            )
            conn.autocommit = True
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
            print("PostgreSQL is not ready yet. Waiting 5 seconds...")
            time.sleep(5)
    return conn

conn = create_conn()
cur = conn.cursor()

cur.execute("""
DROP TABLE IF EXISTS clients;
DROP DATABASE IF EXISTS lundi_matin;
CREATE DATABASE lundi_matin;

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    client_address VARCHAR(255) NOT NULL,
    city_postal_code INTEGER NOT NULL CHECK (city_postal_code >= 0),
    city_name VARCHAR(255) NOT NULL,
    phone_number BIGINT NOT NULL CHECK (phone_number >= 0)
);
""")

conn.commit()
cur.close()
conn.close()
