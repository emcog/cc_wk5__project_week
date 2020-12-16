import pdb
from models.customer import Customer
from models.address import Address  


import repositories.repository_customer as repository_customer

# delete all customer data
# delete all address data



# create address (this is a FK)
address_1 = Address('Knowledge Cottage',    'The Orchard',      'Crail',    'HE3 H11')
address_2 = Address('Minotaur View',        'Labyrinth',        'Crail',    'HE3 H11')
address_3 = Address('Stoney lookout',       'Sarpedon Street',  'Crail',    'HE3 H11')
address_4 = Address('Ray house',            'The Sun',          'Crail',    'HE3 H11')
address_5 = Address('Foamy place',          'Firth of Forth',   'Crail',    'HE3 H11')

# create customer object 
customer_1 = Customer('Eve',        'eve@genesis.god')
customer_2 = Customer('Ariadne',    'goldenthread@greek.myth')
customer_3 = Customer('Medussa',    'badhairday@greek.myth')
customer_4 = Customer('Alectrona',  'shinnyhappypeople@greek.myth')
customer_5 = Customer('Aphrodite',  'love@greek.myth')


#  save(address, delivery_day_id, subscription_id, customer):
repository_customer.save(address_1, 2, 2, customer_1)
repository_customer.save(address_2, 1, 1, customer_2)
repository_customer.save(address_3, 1, 1, customer_3)
repository_customer.save(address_4, 2, 2, customer_4)
repository_customer.save(address_5, 3, 3, customer_5)


# display data to make sure its written
print(repository_customer.select_by_day(1))
