from menu import get_menu, display_menu
from order import get_order
from calculation import calculate_total, calculate_discount
from receipt import print_receipt


def main():

    menu = get_menu()

    print("==========================================")
    print("       WELCOME TO JOLLIBEE!")
    print("       RESTAURANT ORDERING SYSTEM")
    print("==========================================")

    display_menu(menu)

    while True:

        choice = input("\nDo you want to order? (yes/no): ").lower()

        if choice == "yes" or choice == "y":
            break

        elif choice == "no" or choice == "n":
            print("\nThank you for visiting Jollibee!")
            print("Have a nice day!")
            return

        else:
            print("Please enter yes or no.")

    orders = get_order(menu)

    subtotal = calculate_total(orders, menu)

    discount = calculate_discount(subtotal)

    total = subtotal - discount

    print_receipt(
        orders,
        menu,
        subtotal,
        discount,
        total
    )


if __name__ == "__main__":
    main()