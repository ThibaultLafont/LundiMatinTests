import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST")
)
cur = conn.cursor()

#GENERAL
def reorder_client_ids():
    cur.execute("SELECT client_id FROM clients ORDER BY client_id")
    clients = cur.fetchall()
    for index, client in enumerate(clients, start=1):
        cur.execute("UPDATE clients SET client_id = %s WHERE client_id = %s", (index, client[0]))
    conn.commit()


# DELETE QUERY
def delete_client_from_db(client_id):
    cur.execute("DELETE FROM clients WHERE client_id = %s", (client_id,))
    conn.commit()


# UPDATE QUERY
def update_client(client_id, client_name, client_address, city_postal_code, city_name, phone_number):
    cur.execute('UPDATE clients SET client_name = %s, client_address = %s, city_postal_code = %s, city_name = %s, phone_number = %s WHERE client_id = %s',
        (client_name, client_address, city_postal_code, city_name, phone_number, client_id))
    conn.commit()

def fetch_client_from_id(client_id):
    cur.execute('SELECT * FROM clients WHERE client_id = %s', (client_id,))
    client = cur.fetchone()
    return client


# VIEW QUERY
def fetch_client(client_id):
    cur.execute("SELECT * FROM clients WHERE client_id = %s", (client_id,))
    client = cur.fetchone()
    if client:
        client_data = {
            "client_id": client[0],
            "client_name": client[1],
            "client_address": client[2],
            "city_postal_code": client[3],
            "city_name": client[4],
            "phone_number": client[5]
        }
        return client_data
    else:
        return None


#CREATE QUERY
def create_query(client_name, client_address, city_postal_code, city_name, phone_number):
    cur.execute("INSERT INTO clients (client_name, client_address, city_postal_code, city_name, phone_number) VALUES (%s, %s, %s, %s, %s)",
        (client_name, client_address, city_postal_code, city_name, phone_number))
    conn.commit()
    cur.execute('SELECT * FROM clients')
    reorder_client_ids()
    return None