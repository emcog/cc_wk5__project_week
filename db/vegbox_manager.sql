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
    delivery_day_id SERIAL PRIMARY KEY,
    day_of_week VARCHAR(255)
);


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
    address_id INT REFERENCES addresses(id),
    -- delivery_day_id INT REFERENCES delivery_days(id),
    -- subscription_id INT REFERENCES subscription(id)
);


CREATE TABLE subscriptions (
    subscription_id SERIAL PRIMARY KEY,
    -- Foreign keys
    customer_id INT REFERENCES customers(id)
    delivery_day_id INT REFERENCES delivery_days(delivery_day_id)

)