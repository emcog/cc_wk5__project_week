-- DROP TABLE IF EXISTS notes_delivery_to_customer;
-- DROP TABLE IF EXISTS notes_customer_to_delivery;
-- DROP TABLE IF EXISTS subscriptions;
-- DROP TABLE IF EXISTS customers;
-- DROP TABLE IF EXISTS delivery_days;
-- -- DROP TABLE IF EXISTS subscription;
-- DROP TABLE IF EXISTS subscription_type;
-- DROP TABLE IF EXISTS addresses;



CREATE TABLE addresses (
    address_id SERIAL PRIMARY KEY,
    first_line VARCHAR(255),
    second_line VARCHAR(255),
    town_city VARCHAR(255),
    postcode VARCHAR(255)
);


-- populate manually using postico
CREATE TABLE delivery_days (
    delivery_day_id SERIAL PRIMARY KEY,
    day_of_week VARCHAR(255)
);

-- this will be replaced by subscription_types
CREATE TABLE subscription (
    id SERIAL PRIMARY KEY,
    -- pass Null on creeation of customer to indicate not paid
    -- TODO change this boolean to int with a check value as null can cause problems
    -- SELECT ALL FROM CUSTOMER WHERE (subscription_id, delivery_day_id) =  (2, 1) 
    csa_subscription BOOLEAN
);


-- subscription_type replaces subscription
CREATE TABLE subscription_types (
    subscription_type_id SERIAL PRIMARY KEY,
    subscription_type VARCHAR(255)
);


CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    first_name VARCHAR(255),
    -- Foreign keys
    customer_address_id INT REFERENCES addresses(address_id)
    -- delivery_day_id INT REFERENCES delivery_days(id),
    -- subscription_id INT REFERENCES subscription(id)
);


CREATE TABLE subscriptions (
    subscription_id SERIAL PRIMARY KEY,
    start_subscription DATE,  
    end_subscription DATE,
    -- Foreign keys
    customer_subscription_id INT REFERENCES customers(customer_id),
    delivery_subscription_day_id INT REFERENCES delivery_days(delivery_day_id)
);


CREATE TABLE notes_customer_to_delivery (
    notes_customer_to_delivery_id SERIAL PRIMARY KEY,
    note_to_driver TEXT,
    note_created DATE,
    start_change DATE,
    end_change DATE,
    -- Foreign keys
    customer_c_to_d_id INT REFERENCES customers(customer_id),
    normal_address_id INT REFERENCES addresses(address_id),
    temporary_address_id INT REFERENCES addresses(address_id)
);


CREATE TABLE notes_delivery_to_customer (
    notes_delivery_to_customer_id SERIAL PRIMARY KEY,
    note_to_customer TEXT,
    note_created DATE,
    -- Foreign keys
    customer_d_to_n_id INT REFERENCES customers(customer_id)
);