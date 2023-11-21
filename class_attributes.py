class Item:
    # Define a class attribute
    # This attribute is shared amongst all the instances of the class
    pay_rate = 0.8 # The pay rate after 20% discount
    
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
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
item1 = Item("Mobile", 300, 2)
item2 = Item("Laptop", 1500, 3)

# Ways of aAccessing Class Attributes
print(Item.pay_rate)
print(item1.pay_rate)
# print(item2.pay_rate)

# Get all the attributes on the class level
print(Item.__dict__)

# Get all the attributes on the instance level
print(item1.__dict__)