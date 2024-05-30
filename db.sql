CREATE DATABASE lundi_matin;

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    client_address VARCHAR(255) NOT NULL,
    city_postal_code INTEGER NOT NULL CHECK (city_postal_code >= 0),
    city_name VARCHAR(255) NOT NULL,
    phone_number BIGINT NOT NULL CHECK (phone_number >= 0)
);
