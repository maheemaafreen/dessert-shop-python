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
        print(f"{order[1]} x {order[0]} = £{item_total}")
    original_total = grand_total
    final_total = original_total
    if grand_total >= 10:
        final_total = grand_total * 0.9
        discount = original_total - final_total
        print(f"10% DISCOUNT: -£{discount}")
    print(f"FINAL TOTAL: £{final_total}")

def place_order():
    order = input("What dessert would you like? ").lower()
    if order in foods:
        print("Perfect, will do!")
        quan = get_quantity()
        orders.append([order, quan])
        price = get_price(order)
        total = calc_total(price, quan)
        print("Coming up! Your total is £", total)
        return total
    else:
        print("Sorry! We don't have that!")
        return 0


greet(name)
while again == "yes":
    total = place_order()
    grand_total += total
    again = input("Would you like to place another order? (yes/no): ")

receipt()
