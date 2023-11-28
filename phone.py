from item import Item

class Phone(Item):
    def __init__(
            self,
            name: str,
            price: float,
            quantity = 0,
            broken_phones = 0
    ) -> None:
        # Call to super() method to call constructor of the super class
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater than or equal to 0"
        
        # Assign object properties to self
        # Also called as INSTANCE ATTRIBUTES
        self.broken_phones = broken_phones

# phone1 = Phone("jscPhonev10", 500, 5, 1)
# print(Item.all)
# print(Phone.all)
# print(phone1.calculate_total_price())
# phone2 = Phone("jscPhonev20", 700, 3, 2)