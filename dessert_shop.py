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
    print("~YOUR ORDER~")
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
            order = int(input("What dessert would you like? "))
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
        print(f"{number}.{food} : £{get_price(food):.2f}")
    print("~~~~~")

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

receipt()
