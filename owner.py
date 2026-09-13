def save_sales(orders):
    with open("../src/sales.txt", "a") as file:
        for order in orders:
            total = order[0].calculate_total(order[1])
            file.write(f"{order[0].name}, {order[1]}, {total:.2f}\n")

def owner_login(password):
    while True:
        passw = input("Please enter your password: ")
        if passw == password:
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

        total_revenue = sum(revenue_by_dessert.values())
        total_units = sum(quantity_by_dessert.values())
        if total_units > 0:
            average_revenue = total_revenue / total_units
        else:
            average_revenue = 0

        print("\n~~ SALES DASHBOARD ~~")
        for dessert, revenue in revenue_by_dessert.items():
            print(f"{dessert}: £{revenue:.2f}")
        print(f"\nThe bestseller is {best_dessert.lower()}, with £{highest_revenue:.2f} total revenue!")
        print(f"The most sold dessert is {most_sold.lower()}, with {highest_quantity} units sold!")
        print(f"Average revenue per unit: £{average_revenue:.2f}.")
        print(f"Total revenue: £{total_revenue:.2f}.")
        for dessert, revenue in revenue_by_dessert.items():
            percentage = (revenue / total_revenue) * 100
            print(f"~>{dessert}: {percentage:.1f}% of total revenue.")
        print(f"Total units sold: {total_units} units.")

def show_inventory(desserts):
    print("~~ INVENTORY ~~")
    for dessert in desserts:
        if dessert.stock <= 5:
            print(f"{dessert.name}: {dessert.stock} in stock ⚠️LOW IN STOCK!")
        else:
            print(f"{dessert.name}: {dessert.stock} in stock.")
    print("~~~~~~~~~~~~~~~")

def save_inventory(desserts):
    with open("../src/inventory.txt", "w") as file:
        for dessert in desserts:
            file.write(f"{dessert.name}, {dessert.stock}\n")

def load_inventory(desserts):
    with open("../src/inventory.txt", "r") as file:
        for line in file:
            name, stock = line.strip().split(",")
            for dessert in desserts:
                if dessert.name == name:
                    dessert.stock = int(stock)