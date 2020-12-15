
import unittest
from models.address import Address

class TestAddressClass(unittest.TestCase):
    def setUp(self):
        self.address_1 = Address('Knowledge Cottage', 'The Orchard', 'Crail', 'HE3 H11')
        self.address_2 = Address('Minotaur View', 'The Labyrinth', 'Crete-on-Fife', 'FL1 H07')

    def test_address_has_town(self):
        self.assertEqual('Crail', address_1.town_city)