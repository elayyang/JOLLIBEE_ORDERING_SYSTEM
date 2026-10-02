def print_receipt(orders, menu, subtotal, discount, total):

    print("\n")
    print("==========================================")
    print("             JOLLIBEE")
    print("          ORDER RECEIPT")
    print("==========================================")
    print("Date: September 2, 2026")
    print("------------------------------------------")

    print(f"{'Item':<18} {'Qty':>4} {'Price':>8} {'Total':>10}")
    print("------------------------------------------")

    for item, quantity in orders.items():

        price = menu[item]
        item_total = price * quantity

        print(
            f"{item:<18} {quantity:>4} "
            f"₱{price:>7.2f} ₱{item_total:>9.2f}"
        )

    print("------------------------------------------")
    print(f"{'Subtotal:':<30} ₱{subtotal:>9.2f}")
    print(f"{'Discount:':<30} ₱{discount:>9.2f}")
    print("------------------------------------------")
    print(f"{'TOTAL:':<30} ₱{total:>9.2f}")
    print("==========================================")
    print("        Thank you for ordering!")
    print("             Please come again!")
    print("==========================================")