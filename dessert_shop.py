class Dessert:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def calculate_total(self, quantity):
        return self.price * quantity

ice_cream = Dessert("Ice Cream", 2, "frozen")
chocolate = Dessert("Chocolate", 1, "candy")
brownies = Dessert("Brownies", 3, "baked")
cookies = Dessert("Cookies", 2, "baked")
cake = Dessert("Cake", 5, "baked")
desserts = [ice_cream, chocolate, brownies, cookies, cake]

again = "yes"
grand_total = 0
orders = []
password = "Maheema2607"

# FUNCTIONS
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
            print("Oops! Please enter a number.")

def receipt():
    print("Thanks for buying! Here's your receipt:")
    print("~YOUR RECEIPT~")
    for order in orders:
        item_total = order[1] * order[0].price
        print(f"{order[1]} x {order[0].name.lower()} = £{item_total:.2f}")
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
            order = desserts[order-1]
            print(f"Perfect, {order.name.lower()}!")
            quan = get_quantity()
            orders.append([order, quan])
            total = order.calculate_total(quan)
            print(f"Coming up! That'll be £{total:.2f}")
            return total
        except ValueError:
            print("Oops! Please enter a number.")

def show_menu():
    print("~~MENU~~")
    for number, dessert in enumerate(desserts, 1):
        print(f"{number}. {dessert.name} ({dessert.category}): £{dessert.price:.2f}")
    print("~~~~~")

def show_order():
    print("~~YOUR ORDER~~")
    for number, order in enumerate(orders, 1):
        print(f"{number}. {order[1]} x {order[0].name}")

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
                    removed_total += removed[0].price * removed[1]
                    print(f"Done! {removed[1]} x {removed[0].name} has been removed.")
                    show_order()
                    remove_again = input("Would you like to remove another order? (yes/no): ").lower().strip()
                    while remove_again != "yes" and remove_again != "no":
                        remove_again = input("Sorry, I didn't get that! Please enter 'yes' or 'no': ")
                    break
                except ValueError:
                    print("Oops! Please enter a number.")
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
                    old_total = orders[choice2][0].price * old_quantity
                    orders[choice2][1] = new_quantity
                    new_total = orders[choice2][0].price * new_quantity
                    change_in_total = new_total - old_total
                    total_change += change_in_total
                    show_order()
                    change_again = input("Would you like to change the quantity of another item? (yes/no): ").lower().strip()
                    while change_again != "yes" and change_again != "no":
                        change_again = input("Sorry, I didn't get that! Please enter 'yes' or 'no': ")
                    break
                except ValueError:
                    print("Oops! Please enter a number.")
        return total_change
    return 0

def intro():
    while True:
        ppl = input("Hello! Are you a customer, or the owner? ").lower().strip()
        if ppl == "owner" or ppl == "customer":
            return ppl
        else:
            print("Oops! Please enter either 'customer' or 'owner'!")

def owner_login():
    while True:
        passw = input("Please enter your password: ")
        if passw == "Maheema2607":
            return True
        else:
            print("Incorrect password.")

def sales_analysis():
    with open("../src/sales.txt", "r") as file:
        content = file.read().splitlines()
        revenue_by_dessert = {}
        quantity_by_dessert = {}
        highest_revenue = 0
        best_dessert = ""
        highest_quantity = 0
        most_sold = ""
        total_revenue = 0
        total_units = 0

        for sale in content:
            parts = sale.split(",")
            dessert = parts[0]
            quantity = int(parts[1])
            revenue = float(parts[2])
            if dessert not in revenue_by_dessert:
                revenue_by_dessert[dessert] = 0
            revenue_by_dessert[dessert] += revenue
            if dessert not in quantity_by_dessert:
                quantity_by_dessert[dessert] = 0
            quantity_by_dessert[dessert] += quantity

        for dessert, revenue in revenue_by_dessert.items():
            if revenue > highest_revenue:
                highest_revenue = revenue
                best_dessert = dessert

        for dessert, quantity in quantity_by_dessert.items():
            if quantity > highest_quantity:
                highest_quantity = quantity
                most_sold = dessert

        for dessert, revenue in revenue_by_dessert.items():
            total_revenue += revenue
        for dessert, quantity in quantity_by_dessert.items():
            total_units += quantity

        print(revenue_by_dessert)
        print(f"The bestseller is {best_dessert.lower()}, with £{highest_revenue:.2f} total revenue!")
        print(f"The most sold dessert is {most_sold.lower()}, with {highest_quantity} units sold!")
        print(f"Total revenue: £{total_revenue:.2f}.")
        print(f"Total units sold: {total_units} units.")

def save_sales():
    with open("../src/sales.txt", "a") as file:
        for order in orders:
            total = order[0].calculate_total(order[1])
            file.write(f"{order[0].name}, {order[1]}, {total:.2f}\n")


ppl = intro()
if ppl == "owner":
    print("Welcome, owner!")
    logged_in = owner_login()
    if logged_in:
        print("Access granted!")
        sales_analysis()
else:
    name = input("What's your name?: ").strip()
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
    save_sales()
    receipt()
