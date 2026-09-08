foods = ["ice cream", "chocolate", "brownies", "cookies", "cake"]
prices = {"ice cream":2, "chocolate":1, "brownies": 3, "cookies" : 2, "cake" :5}
again = "yes"
grand_total = 0
orders = []
name = input("Hi, what's your name? :")
def greet(name):
    print(f"Hello, {name}! Welcome to the dessert shop!")
greet(name)
while again == "yes":
    order = input("What dessert would you like?")
    if order in foods:
        print("Perfect, will do!")
        quan = int(input("How many would you like? : "))
        while quan <= 0:
            quan = int(input("Sorry, that's not a valid quantity! What quantity would you like? : "))
        orders.append([order, quan])
        price = prices[order]
        total = price * quan
        grand_total += total
        print("Coming up! Your total is £", total)
    else:
        print("Sorry! We don't have that!")
    again = input("Would you like to place another order? (yes/no): ")
def receipt():
    print("Thanks for buying! Here's your receipt:")
    print("~YOUR ORDER~")
    for order in orders:
        print(f"{order[1]} x {order[0]}")
    print(f"GRAND TOTAL: £{grand_total}")
receipt()
