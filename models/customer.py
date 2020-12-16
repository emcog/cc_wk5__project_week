class Customer:

    def __init__( self, first_name, email, subscription_type = None, delivery_day_id = None, id = None ):
        self.first_name = first_name
        self.email = email
        self.subscription_type = subscription_type
        self.delivery_day_id = delivery_day_id
        self.id = id        
