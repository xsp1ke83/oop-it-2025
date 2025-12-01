def process_order(price, quantity):
    print("Order received")
    total = calculate_total(price, quantity)
    handle_discount(total)

def calculate_total(price, quantity):
    total = price * quantity
    print(f"Total price: {total}")
    return total

def handle_discount(total):
    if total > 100:
        print("Discount applied")
