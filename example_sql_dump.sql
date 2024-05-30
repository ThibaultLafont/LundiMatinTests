CREATE DATABASE lundi_matin;

USE lundi_matin;

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    client_address VARCHAR(255) NOT NULL,
    city_postal_code INTEGER NOT NULL CHECK (city_postal_code >= 0),
    city_name VARCHAR(255) NOT NULL,
    phone_number BIGINT NOT NULL CHECK (phone_number >= 0)
);


INSERT INTO clients (client_name, client_address, city_postal_code, city_name, phone_number)
VALUES 
('Alice Smith', '123 Maple Street', 12345, 'Mapleton', 0734567890),
('Bob Johnson', '456 Oak Avenue', 67890, 'Oakville', 0645678901);