class Address:
   
    def __init__(self, first_line, second_line, town_city, postcode, id = None):
        self.first_line = first_line
        self.second_line = second_line
        self.town_city = town_city
        self.postcode = postcode
        self.id = id


    def full_address(self):
        return f"{self.first_line} {self.second_line} {self.town_city} {self.postcode}"

