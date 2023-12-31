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
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
item1 = Item("Mobile", 100, 2)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
# Update the pay_rate Class Attribute here (instance attribute)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)