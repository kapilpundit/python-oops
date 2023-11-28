import csv

class Item:
    # Define a class attribute
    # This attribute is shared amongst all the instances of the class
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    
    '''
    Ref: https://www.youtube.com/watch?v=Ej_02ICOIgs&t=1977s
    Define the constructor with _init__() method
    Type hint the parameters. name should be str, price should be float,
    and as we have already defined the default value of quantity as 0 which is int.
    '''
    def __init__(self, name: str, price: float, quantity = 0) -> None:
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {price} is not greater than or equal to 0"
        
        # Assign object properties to self
        # Also called as INSTANCE ATTRIBUTES
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        '''
        property decorator to restrict changes to the name attribute
        name is a private member so can not be updated through an instance
        '''
        print(f"Getting name attribute's value '{self.__name}'")
        return self.__name
    
    @name.setter
    def name(self, value):
        '''
        @name.setter decorator is used to update the value of the __name
        private member through an instance
        Ex. item1.name = "Other name"
        '''

        # Restrict name to value upto 10 characters
        if len(value) > 10:
            raise Exception("The value of name should be upto 10 characters")
        
        print(f"Updating name attribute's value to '{value}'")
        self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod    
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.price}, {self.quantity}')"
        
    def __str__(self):
        return f"Item('{self.name}, {self.price}, {self.quantity}')"
