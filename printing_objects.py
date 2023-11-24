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
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        self.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# Print name attribute of all the instances
for inst in Item.all:
    print(inst.name)