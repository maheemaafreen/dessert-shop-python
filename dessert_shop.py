foods = ["ice cream", "chocolate", "brownies", "cookies", "cake"]
prices = {"ice cream":2, "chocolate":1, "brownies": 3, "cookies" : 2, "cake" :5}
again = "yes"
grand_total = 0
orders = []
name = input("Hi, what's your name? : ").strip()

# FUNCTIONS
def calc_total(price, quan):
    return price * quan

def greet(name):
    print(f"Hello, {name}! Welcome to the dessert shop!")

def get_quantity():
    while True:
        try:
            quan = int(input("How many would you like? : "))
            while quan <= 0:
                quan = int(input("Sorry, that's not a valid quantity! What quantity would you like? : "))
            return quan
        except ValueError:
            print("Oops! Please enter a number: ")

def get_price(order):
    return prices[order]

def receipt():
    print("Thanks for buying! Here's your receipt:")
    print("~YOUR RECEIPT~")
    for order in orders:
        item_total = order[1] * get_price(order[0])
        print(f"{order[1]} x {order[0]} = £{item_total:.2f}")
    original_total = grand_total
    final_total = original_total
    if grand_total >= 10:
        final_total = grand_total * 0.9
        discount = original_total - final_total
        print(f"10% DISCOUNT: -£{discount:.2f}")
    print(f"FINAL TOTAL: £{final_total:.2f}")

def place_order():
    while True:
        try:
            order = int(input("What dessert would you like? (Enter its number): "))
            while order < 1 or order > 5:
                order = int(input("Oops! Please enter a number between 1-5 : "))
            order = foods[order-1]
            print(f"Perfect, {order}!")
            quan = get_quantity()
            orders.append([order, quan])
            price = get_price(order)
            total = calc_total(price, quan)
            print(f"Coming up! That'll be £{total:.2f}")
            return total
        except ValueError:
            print("Oops! Please enter a number: ")

def show_menu():
    print("~~MENU~~")
    for number,food in enumerate(foods, 1):
        print(f"{number}. {food} : £{get_price(food):.2f}")
    print("~~~~~")

def show_order():
    print("~~YOUR ORDER~~")
    for number, order in enumerate(orders, 1):
        print(f"{number}. {order[1]} x {order[0]}")

def remove_order():
    print("~~REMOVE ORDER~~")
    remove = input("Would you like to remove an item? (yes/no): ").lower().strip()
    while remove!="yes" and remove!="no":
        print("Sorry, I didn't get that! Please enter 'yes' or 'no'")
        remove = input("Would you like to remove an item? (yes/no): ").lower().strip()
    removed_total = 0
    if remove == "yes":
        remove_again = "yes"
        while remove_again == "yes":
            while True:
                try:
                    choice = int(input("Please enter the number of the order you'd like to remove: "))
                    while choice < 1 or choice > len(orders):
                        choice = int(input("Oops! Please choose a number that is on your order list: "))
                    choice = choice - 1
                    removed = orders.pop(choice)
                    removed_total += get_price(removed[0]) * removed[1]
                    print(f"Done! {removed[1]} x {removed[0]} has been removed.")
                    show_order()
                    remove_again = input("Would you like to remove another order? (yes/no): ").lower().strip()
                    while remove_again != "yes" and remove_again != "no":
                        remove_again = input("Sorry, I didn't get that! Please enter 'yes' or 'no': ")
                    break
                except ValueError:
                    print("Oops! Please enter a number: ")
        return removed_total
    return 0

def change_quantity():
    print("~~CHANGE QUANTITY~~")
    change = input("Would you like to change the quantity of an item? (yes/no): ").lower().strip()
    while change != "yes" and change != "no":
        print("Sorry, I didn't get that! Please enter 'yes' or 'no'")
        change = input("Would you like to change the quantity of an item? (yes/no): ").lower().strip()
    total_change = 0
    if change == "yes":
        change_again = "yes"
        while change_again == "yes":
            while True:
                try:
                    choice2 = int(input("Please enter the number of the order you wish to edit: "))
                    while choice2 < 1 or choice2 > len(orders):
                        choice2 = int(input("Oops! Please choose a number that is on your order list: "))
                    choice2 = choice2 - 1
                    new_quantity = get_quantity()
                    old_quantity = orders[choice2][1]
                    old_total = get_price(orders[choice2][0]) * old_quantity
                    orders[choice2][1] = new_quantity
                    new_total = get_price(orders[choice2][0]) * new_quantity
                    change_in_total = new_total - old_total
                    total_change += change_in_total
                    show_order()
                    change_again = input("Would you like to change the quantity of another item? (yes/no): ").lower().strip()
                    while change_again != "yes" and change_again != "no":
                        change_again = input("Sorry, I didn't get that! Please enter 'yes' or 'no': ")
                    break
                except ValueError:
                    print("Oops! Please enter a number: ")
        return total_change
    return 0


greet(name)
show_menu()
while again == "yes":
    total = place_order()
    grand_total += total
    print(f"Current total: £{grand_total:.2f}")
    again = input("Would you like to place another order? (yes/no): ").lower().strip()
    while again!="yes" and again!="no":
        print("Sorry, I didn't get that! Please enter 'yes' or 'no'")
        again = input("Would you like to place another order? (yes/no): ").lower().strip()
show_order()
grand_total -= remove_order()
grand_total += change_quantity()
receipt()
