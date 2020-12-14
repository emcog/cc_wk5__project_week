DROP TABLE IF EXISTS addresses;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS deliveries;


CREATE TABLE deliveries (
    id SERIAL PRIMARY KEY,
    day_of_week VARCHAR(255),
    -- day_of_week VARCHAR CONSTRAINT three_characters CHECK (day_of_week = 3),
    vegboxes INT CHECK (vegboxes >= 0)
);


CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    first_name VARCHAR(255),
    -- pass Null on creeation of customer to indicate not paid
    csa_subscription BOOLEAN,
    -- Foreign key
    customer_address INT REFERENCES addresses(id)
);


CREATE TABLE addresses (
    id SERIAL PRIMARY KEY
    first_line VARCHAR(255),
    second_line VARCHAR(255),
    town_city VARCHAR(255),
    postcode VARCHAR(255)
);