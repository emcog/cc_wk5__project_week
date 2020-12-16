DROP TABLE IF EXISTS customers;
-- DROP TABLE IF EXISTS delivery_days;
-- DROP TABLE IF EXISTS subscription;
DROP TABLE IF EXISTS addresses;



CREATE TABLE addresses (
    id SERIAL PRIMARY KEY,
    first_line VARCHAR(255),
    second_line VARCHAR(255),
    town_city VARCHAR(255),
    postcode VARCHAR(255)
);


-- populate manually using postico
CREATE TABLE delivery_days (
    id SERIAL PRIMARY KEY,
    day_of_week VARCHAR(255)
);


CREATE TABLE subscription (
    id SERIAL PRIMARY KEY,
    -- subscription
    -- pass Null on creeation of customer to indicate not paid
    csa_subscription BOOLEAN
);


CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    first_name VARCHAR(255),
    -- pass Null on creeation of customer to indicate not paid
    -- csa_subscription BOOLEAN,
    -- Foreign keys
    address_id INT REFERENCES addresses(id),
    delivery_day_id INT REFERENCES delivery_days(id),
    subscription_id INT REFERENCES subscription(id)
);