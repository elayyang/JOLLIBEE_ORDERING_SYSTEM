def display_menu(menu):
    print("\n==========================================")
    print("             JOLLIBEE MENU")
    print("==========================================")

    print(f"{'Item':<25} {'Price':>10}")
    print("------------------------------------------")

    for item, price in menu.items():
        print(f"{item:<25} ₱{price:>8.2f}")

    print("==========================================")


def get_menu():
    return {
        "Chickenjoy": 99.00,
        "Jolly Spaghetti": 60.00,
        "Burger Steak": 75.00,
        "Yumburger": 45.00,
        "Jolly Hotdog": 65.00,
        "Peach Mango Pie": 45.00,
        "Fries": 50.00,
        "Coke": 40.00
    }