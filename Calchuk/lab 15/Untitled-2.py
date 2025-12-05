def calculate_tax(order):
    return order.price * 0.2

def calculate_discount(order):
    return order.price * 0.1 if order.price > 1000 else 0

def process_order(order):
    print("Processing order...")
    tax = calculate_tax(order)
    discount = calculate_discount(order)
    total = order.price + tax - discount
    print(f"Total: {total}")
    return total
