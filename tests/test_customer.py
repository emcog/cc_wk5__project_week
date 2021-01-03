import unittest
from models.customer import Customer

class TestCustomerClass(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer('Ariadne', 'goldenthread@greek.myth')
        self.customer_2 = Customer('Medussa', 'badhairday@greek.myth')


    def test_customer_has_name(self):
        self.assertEqual('Ariadne', self.customer_1.first_name)

    def test_customer_has_email(self):
        self.assertEqual('badhairday@greek.myth', self.customer_2.email)