from models import Dessert
from order import show_menu, get_yes_no, place_order, show_order, remove_order, change_quantity, receipt
from owner import save_sales, owner_login, sales_analysis

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

def intro():
    while True:
        ppl = input("Hello! Are you a customer, or the owner? ").lower().strip()
        if ppl == "owner" or ppl == "customer":
            return ppl
        else:
            print("Oops! Please enter either 'customer' or 'owner'!")

ppl = intro()
if ppl == "owner":
    print("Welcome, owner!")
    logged_in = owner_login(password)
    if logged_in:
        print("Access granted!")
        sales_analysis()
else:
    name = input("What's your name?: ").strip()
    greet(name)
    show_menu(desserts)
    while again == "yes":
        total = place_order(desserts, orders)
        grand_total += total
        print(f"Current total: £{grand_total:.2f}")
        again = get_yes_no("Would you like to place another order? (yes/no): ")
    show_order(orders)
    grand_total -= remove_order(orders)
    grand_total += change_quantity(orders)
    save_sales(orders)
    receipt(grand_total, orders)