def process_order(order):
    print("Processing order...")

    # розрахунок податку
    tax = order.price * 0.2
    print(f"Tax: {tax}")

    # перевірка знижки
    if order.price > 1000:
        discount = order.price * 0.1
        print(f"Discount applied: {discount}")
    else:
        discount = 0

    total = order.price + tax - discount
    print(f"Total: {total}")
    return total
