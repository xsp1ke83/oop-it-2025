def process_order(price, quantity):
    print("Order received")
    total = price * quantity
    print(f"Total price: {total}")
    if total > 100:
        print("Discount applied")
