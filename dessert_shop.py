foods = ["ice cream", "chocolate", "brownies", "cookies", "cake"]
prices = {"ice cream":2, "chocolate":1, "brownies": 3, "cookies" : 2, "cake" :5}
again = "yes"
grand_total = 0
orders = []
name = input("Hi, what's your name? : ")

# FUNCTIONS
def calc_total(price, quan):
    return price * quan

def greet(name):
    print(f"Hello, {name}! Welcome to the dessert shop!")

def get_quantity():
    quan = int(input("How many would you like? : "))
    while quan <= 0:
        quan = int(input("Sorry, that's not a valid quantity! What quantity would you like? : "))
    return quan

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
    order = input("What dessert would you like? ").lower()
    if order in foods:
        print("Perfect, will do!")
        quan = get_quantity()
        orders.append([order, quan])
        price = get_price(order)
        total = calc_total(price, quan)
        print(f"Coming up! Your total is £{total:.2f}")
        return total
    else:
        print("Sorry! We don't have that!")
        return 0

def show_menu():
    print("~~MENU~~")
    for food in foods:
        print(f"{food} : £{get_price(food):.2f}")
    print("~~~~~")

greet(name)
show_menu()
while again == "yes":
    total = place_order()
    grand_total += total
    again = input("Would you like to place another order? (yes/no): ").lower()
    while again!="yes" and again!="no":
        print("Sorry, I didn't get that! Please enter 'yes' or 'no'")
        again = input("Would you like to place another order? (yes/no): ").lower()

receipt()
