from menu import display_menu


def get_order(menu):
    orders = {}

    while True:
        display_menu(menu)

        print("\nAvailable items:")

        for item in menu:
            print("-", item)

        item = input("\nEnter the menu item: ").strip()

        if item not in menu:
            print("\nInvalid menu item. Please choose from the menu.")
            continue

        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                else:
                    break

            except ValueError:
                print("Invalid quantity. Please enter a number.")

        if item in orders:
            orders[item] += quantity
        else:
            orders[item] = quantity

        print(f"\nAdded {quantity} x {item} to your order.")

        while True:
            another = input(
                "\nDo you want to order another item? (yes/no): "
            ).lower()

            if another == "yes" or another == "y":
                break

            elif another == "no" or another == "n":
                return orders

            else:
                print("Please enter yes or no.")