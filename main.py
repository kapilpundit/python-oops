from item import Item
# from phone import Phone

item1 = Item("myItem", 500, 2)
item1.name = "Other Item"

# This will raise AttributeError: 'Item' object has no attribute '__connect'
# Because __connect() is a private method (with leading double underscores)
# item1.__connect("Yahoo")
item1.send_email()


# This will raise an exception, because value of name can be upto 10 characters only
# item1.name = "Other Item name"


# print(item1.name)
