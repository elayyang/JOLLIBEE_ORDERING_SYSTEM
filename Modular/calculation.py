def calculate_total(orders, menu):
    subtotal = 0

    for item, quantity in orders.items():
        subtotal += menu[item] * quantity

    return subtotal


def calculate_discount(subtotal):
    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    return discount