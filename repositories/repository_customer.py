from db.run_sql import run_sql

from models.address import Address
from models.customer import Customer


# def drop_and_create():



# create an address
# assign a customer to an address

  #  ---------->
    # Think about from perspective of form
    # this handles data wherever it comes from and adds to tables
    # this handles the passing of data to the database


# refactor into two functions
def save(address,customer):
    # takes in customer object
    # address object
    
    sql_address = 'INSERT INTO addresses (first_line, second_line, town_city, postcode) VALUES (%s, %s, %s, %s) RETURNING *'
    sql_customer = 'INSERT INTO customers (first_name, email, address_id) VALUES (%s, %s, %s) RETURNING *'

    # list of object values passed to run sql function
    values_address = [address.first_line, address.second_line, address.town_city, address.postcode]
 
    # generate address results with sql command
    address_results = run_sql(sql_address, values_address)
    # get foreign key
    address_id = address_results[0]['id']
    # assign fk to customer
    values_customer = [customer.first_name, customer.email, address_id]

    # generate address results with sql command
    customer_results = run_sql(sql_customer, values_customer)
    #  ---> database should be updated


    # refactor to two functions
    # get console up and runnning
    # test with customer 
    # pass bo









def select_all():
    customers = []

    sql = 'SELECT * FROM customers'
    results = run_sql(sql)

    for row in results:
        customer = Customer(row['first_name'], row['email'])
        customers.append(customer)
    return customers





def delete_all():
    sql_address = 'DELETE  FROM addresses'
    sql_customer = 'DELETE  FROM customers'
    run_sql(sql_address, sql_customer)