import pdb
from models.customer import Customer
from models.address import Address  


import repositories.repository_customer as repository_customer

# delete all customer data
# delete all address data

# create address
address_1 = Address('Knowledge Cottage', 'The Orchard', 'Crail', 'HE3 H11')

# create customer object 
customer_1 = Customer('Eve', 'eve@genesis.god')

# save customer and address to db
# 1 = Monday
# 2 = Wednesday
# 3 = Friday
# Id referenced from postico
repository_customer.save(address_1, 1, 1, customer_1)


# display data to make sure its written
repository_customer.select_all()