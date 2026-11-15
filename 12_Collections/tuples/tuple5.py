products = (
    (101, "Laptop", 50000, 2),
    (102, "Mouse", 500, 5),
    (103, "Keyboard", 1000, 3),
    (104, "Monitor", 15000, 2)
)

def display_products():
    for p in products:
        print(p)

def total_cost():
    for p in products:
        cost = p[2] * p[3]
        print(p[1], "=", cost)

def highest_price():
    p = max(products, key=lambda x: x[2])
    print("Highest priced product:", p[1], p[2])

def inventory_value():
    total = 0
    for p in products:
        total = total + (p[2] * p[3])
    print("Total inventory value:", total)

def search_product(pid):
    for p in products:
        if p[0] == pid:
            print("Product found:", p)
            return
    print("Product not found")

def greater_than(amount):
    print("Products with total value greater than", amount)
    for p in products:
        if p[2] * p[3] > amount:
            print(p)

print("Products:")
display_products()

print("\nTotal cost of each product:")
total_cost()

print()
highest_price()

print()
inventory_value()

print()
search_product(102)

print()
greater_than(20000)
