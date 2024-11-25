"""
    In this set of modules, we are learning all about
    `lists` and associated built-in methods.
"""

# We can create a list with:
orders = ["daisies", "periwinkle"]
# And append to that list
orders.append("tulips")

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]

orders_combined = orders + new_orders

#broken_prices = [5, 3, 4, 5, 4] + 4

"""
"""

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist[1] = "Calla"
print(garden_waitlist)
garden_waitlist[-1] = "Alex"
print(garden_waitlist)

"""
"""

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)
new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)
new_store_order_list.remove("Onions")

"""
"""

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]
ages = [["Aaron", 15], ["Dhruti", 16]]

"""
"""

class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)
ellies_score = class_name_test[-1][-1]
print(ellies_score)

incoming_class = [["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]
print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)
incoming_class[-3][-3] = "Ken"
print(incoming_class)

"""
    I really like this a lot! `zip`.
"""

names = ["a", "b", "c"]
nums = [1,2,3]
names_nums = zip(names,nums)
print(names_nums)
