from flask import Blueprint, request, jsonify, render_template, redirect, url_for
import psycopg2
from .queries import create_query, fetch_client, fetch_client_from_id, update_client, reorder_client_ids, delete_client_from_db
from dotenv import load_dotenv
import os

main_blueprint = Blueprint('main', __name__)

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST")
)

def format_phone_number(value):
    phone_str = str(value)
    phone_str = "0" + phone_str
    return " ".join([phone_str[i:i+2] for i in range(0, len(phone_str), 2)])

@main_blueprint.route('/')
def index():
    reorder_client_ids()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()
    return render_template('index.html', clients=clients)


@main_blueprint.route('/delete/<int:client_id>', methods=['GET'])
def delete_client(client_id):
    delete_client_from_db(client_id)
    reorder_client_ids()
    return redirect(url_for('main.index'))


@main_blueprint.route('/edit/<int:client_id>', methods=['GET', 'POST'])
def edit_client(client_id):
    if request.method == 'POST':
        try:
            client_name = request.form['client_name']
            client_address = request.form['client_address']
            city_postal_code = request.form['city_postal_code']
            city_name = request.form['city_name']
            phone_number = request.form['phone_number']
        except KeyError as e:
            return jsonify({"message": "Missing field: {}".format(e)}), 400

        update_client(client_id, client_name, client_address, city_postal_code, city_name, phone_number)
        return redirect(url_for('main.index'))
    if request.method == 'GET':
        client = fetch_client_from_id(client_id)
        return render_template('edit_client.html', client=client)
    return jsonify({"message": "Invalid request"}), 400


@main_blueprint.route('/view/<int:client_id>', methods=['GET'])
def view_client(client_id):
    if not client_id:
        return jsonify({"message": "Client ID is required"}), 400

    client_data = fetch_client(client_id)

    if client_data:
        return render_template('view_client.html', client=client_data)
    else:
        return jsonify({"message": "Client not found"}), 404


@main_blueprint.route('/create', methods=['POST'])
def create():
    client_name = request.form['client_name']
    client_address = request.form['client_address']
    city_postal_code = request.form['city_postal_code']
    city_name = request.form['city_name']
    phone_number = request.form['phone_number']

    create_query(client_name, client_address, city_postal_code, city_name, phone_number)

    return redirect(url_for('main.index'))
