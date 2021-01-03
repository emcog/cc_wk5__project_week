from db.run_sql import run_sql

from models.address import Address

def save_address(address):
    sql = 'INSERT INTO addresses (first_line, second_line, town_city, postcode) VALUES (%s, %s) RETURNING *'
    values = [address.first_line, address.second_line, address.town_city, address.postcode]
    results = (run_sql, values)
    id = results[0]['id']
    address.id = id
    return address

def select_all_addresses():
    addresses = []

    sql = 'SELECT * FROM addresses'
    results = run_sql(sql)

    for row in results:
        address = Address(row['first_line'], row['second_line'], row['town_city'], row['postcode'], row['id'])
        addresses.append(address)
    return addresses