from db.run_sql import run_sql

from models.address import Address
from models.customer import Customer



  #  ---------->
    # This handles data from wherever it comes from and adds to db / tables 
    # Think about from perspective of where is comes from (form, csv, api


    # takes as many object as added to DB
def save(address, delivery_day_id, subscription_id, customer):

    # todo refactor into separate functions
    sql_address = 'INSERT INTO addresses (first_line, second_line, town_city, postcode) VALUES (%s, %s, %s, %s) RETURNING *'
    sql_customer = 'INSERT INTO customers (first_name, email, address_id, delivery_day_id, subscription_id) VALUES (%s, %s, %s, %s, %s) RETURNING *'

    # list of object values passed to run sql function
    values_address = [ address.first_line, address.second_line, address.town_city, address.postcode ]
 
    # generate results with sql command
    address_results = run_sql(sql_address, values_address)
    
    # get foreign keys
    address_id = address_results[0]['id']
    
    # assign fk to customer
    values_customer = [customer.first_name, customer.email, address_id, delivery_day_id, subscription_id]

    # generate address results with sql command
    customer_results = run_sql(sql_customer, values_customer)
    #  ---> database should be updated





def select_all():
    customers = []

    sql = 'SELECT * FROM customers'
    results = run_sql(sql)

    for row in results:
        customer = Customer(row['first_name'], row['email'])
        customers.append(customer)
    return customers



def select_by_day(delivery_day_id):
    customers = []

    sql = 'SELECT * FROM customers WHERE delivery_day_id = %s'
    values =[delivery_day_id]
    results = run_sql(sql, values)

    for row in results:
        # this depends on how its listed on init in class
        #  e.g. def __init__( self, first_name, email, subscription_type = None, id = None ):
        customer = Customer(row['first_name'], row['email'], row['subscription_id'], row['delivery_day_id'], row['id'])
        customers.append(customer)
    return customers


def total_veg_box_by_day(delivery_day_id):
    sql = 'SELECT COUNT(*) FROM customers WHERE delivery_day_id = %s GROUP BY delivery_day_id'
    values =[delivery_day_id]
    results = run_sql(sql, values)
    # returns a dictionary, ['count'] references column name
    return results[0]['count']




def delete_all():
    sql_address = 'DELETE  FROM addresses'
    sql_delivery_day = 'DELETE  FROM delivery_day'
    sql_customer = 'DELETE  FROM customers'
    run_sql(sql_address, sql_customer)


def get_delivery_day_id(day):
    # SELECT id FROM delivery_days WHERE day_of_week = 'monday'
    sql = 'SELECT id FROM delivery_days WHERE day_of_week = %s'
    values = [day]
    results = run_sql(sql, values)

    return results[0]['id']
