class JollibeeSystem:

    def __init__(self):
        self.menu = {
            "Chickenjoy": 99.00,
            "Jolly Spaghetti": 60.00,
            "Burger Steak": 75.00,
            "Yumburger": 45.00,
            "Jolly Hotdog": 65.00,
            "Peach Mango Pie": 45.00,
            "Fries": 50.00,
            "Coke": 40.00
        }

        self.orders = {}

    def display_menu(self):

        print("\n==========================================")
        print("             JOLLIBEE MENU")
        print("==========================================")

        print(f"{'Item':<25} {'Price':>10}")
        print("------------------------------------------")

        for item, price in self.menu.items():
            print(f"{item:<25} ₱{price:>8.2f}")

        print("==========================================")

    def get_order(self):

        while True:

            self.display_menu()

            print("\nAvailable items:")

            for item in self.menu:
                print("-", item)

            item = input("\nEnter the menu item: ").strip()

            if item not in self.menu:
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

            if item in self.orders:
                self.orders[item] += quantity
            else:
                self.orders[item] = quantity

            print(f"\nAdded {quantity} x {item} to your order.")

            while True:

                another = input(
                    "\nDo you want to order another item? (yes/no): "
                ).lower()

                if another == "yes" or another == "y":
                    break

                elif another == "no" or another == "n":
                    return

                else:
                    print("Please enter yes or no.")

    def calculate_total(self):

        subtotal = 0

        for item, quantity in self.orders.items():
            subtotal += self.menu[item] * quantity

        return subtotal

    def calculate_discount(self, subtotal):

        if subtotal >= 500:
            return subtotal * 0.10

        return 0

    def print_receipt(self, subtotal, discount, total):

        print("\n")
        print("==========================================")
        print("             JOLLIBEE")
        print("          ORDER RECEIPT")
        print("==========================================")
        print("Date: September 2, 2026")
        print("------------------------------------------")

        print(
            f"{'Item':<18} "
            f"{'Qty':>4} "
            f"{'Price':>8} "
            f"{'Total':>10}"
        )

        print("------------------------------------------")

        for item, quantity in self.orders.items():

            price = self.menu[item]
            item_total = price * quantity

            print(
                f"{item:<18} "
                f"{quantity:>4} "
                f"₱{price:>7.2f} "
                f"₱{item_total:>9.2f}"
            )

        print("------------------------------------------")

        print(
            f"{'Subtotal:':<30} "
            f"₱{subtotal:>9.2f}"
        )

        print(
            f"{'Discount:':<30} "
            f"₱{discount:>9.2f}"
        )

        print("------------------------------------------")

        print(
            f"{'TOTAL:':<30} "
            f"₱{total:>9.2f}"
        )

        print("==========================================")
        print("        Thank you for ordering!")
        print("             Please come again!")
        print("==========================================")

    def run(self):

        print("==========================================")
        print("       WELCOME TO JOLLIBEE!")
        print("       RESTAURANT ORDERING SYSTEM")
        print("==========================================")

        self.display_menu()

        while True:

            choice = input(
                "\nDo you want to order? (yes/no): "
            ).lower()

            if choice == "yes" or choice == "y":
                break

            elif choice == "no" or choice == "n":

                print("\nThank you for visiting Jollibee!")
                print("Have a nice day!")

                return

            else:
                print("Please enter yes or no.")

        self.get_order()

        subtotal = self.calculate_total()

        discount = self.calculate_discount(subtotal)

        total = subtotal - discount

        self.print_receipt(
            subtotal,
            discount,
            total
        )