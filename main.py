class Item:
    '''
    Define the constructor with _init__() method
    Type hint the parameters. name should be str, price should be float,
    and as we have already defined the default value of quantity as 0 which is int.
    '''
    def __init__(self, name: str, price: float, quantity = 0) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    

item1 = Item("Mobile", 300, 2)
print(item1.calculate_total_price())

item1 = Item("Laptop", 1500, 3)
print(item1.calculate_total_price())