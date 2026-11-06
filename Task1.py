DISCOUNT_PERCENTAGE = 10


def calculate_subtotal(price, quantity):
    return price * quantity


def calculate_discount(subtotal, discount_percentage):
    return subtotal * discount_percentage / 100


def calculate_final_amount(subtotal, discount):
    return subtotal - discount


def format_amount(value):
    return f"{value:.2f}".rstrip("0").rstrip(".")


product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = float(input("Enter quantity: "))

subtotal = calculate_subtotal(price, quantity)
discount = calculate_discount(subtotal, DISCOUNT_PERCENTAGE)
final_amount = calculate_final_amount(subtotal, discount)

print(f"Product: {product_name}")
print(f"Price: {format_amount(price)}")
print(f"Quantity: {format_amount(quantity)}")
print(f"Subtotal: {format_amount(subtotal)}")
print(f"Discount: {format_amount(discount)}")
print(f"Final Amount: {format_amount(final_amount)}")