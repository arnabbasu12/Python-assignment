# Taking customer name
customer_name = input("Enter customer's name: ")
print(f"Hello {customer_name}! Welcome to our shop sir")
# Taking product details
product1 = input("Enter name of product 1: ")
price1 = float(input("Enter price of product 1: "))

product2 = input("Enter name of product 2: ")
price2 = float(input("Enter price of product 2: "))

product3 = input("Enter name of product 3: ")
price3 = float(input("Enter price of product 3: "))


# Calculating subtotal
subtotal = price1 + price2 + price3


# Determining discount
if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0


# Calculating discount amount
discount = subtotal * discount_rate

# Calculating final total
final_total = subtotal - discount


# Displaying shopping summary
print("\n===== SHOPPING SUMMARY =====")

print(f"Customer Name: {customer_name}")

print(f"Product 1: {product1}")
print(f"Price: {price1}")

print(f"Product 2: {product2}")
print(f"Price: {price2}")

print(f"Product 3: {product3}")
print(f"Price: {price3}")

print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Total: {final_total}")