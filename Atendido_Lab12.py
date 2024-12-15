# Food menu with prices
menu = {
    "French Fries": 150.00,
    "Pizza": 300.00,
    "Pasta": 99.00,
    "Lasagna": 150.00,
    "Mojos": 100.00,
    "Burger": 100.00,
    "Chicken": 599.00
}

# Function to display the menu
def display_menu():
    print("Welcome to the Food Ordering System!")
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}:  ₱{price:.2f}")

# Function to get a valid order from the user
def get_order():
    while True:
        order = input("Please choose an item from the menu (or type 'quit' to exit): ").title()
        if order == 'Quit':
            return None
        if order in menu:
            return order
        else:
            print("Invalid selection, please choose a valid item from the menu.")

# Main function to handle the ordering process
def process_order():
    change = 0
    cash_rendered = 0

    while True:
        # Display the menu
        display_menu()

        # Get the user's order
        order = get_order()
        if not order:
            print("Thank you for visiting!")
            break

        # Get the price of the selected item
        price = menu[order]
        print(f"You have selected {order}. The price is ₱{price:.2f}.")

        # Deduct price from change or ask for payment if no funds available
        if cash_rendered == 0:
            while True:
                try:
                    cash_rendered = float(input(f"Please enter the cash rendered to pay for the item (₱{price:.2f}): ₱"))
                    if cash_rendered < price:
                        print("Insufficient funds. Please enter an amount greater than or equal to the total price.")
                    else:
                        change = cash_rendered - price
                        print(f"You have paid ₱{cash_rendered:.2f}. Your change is ₱{change:.2f}.")
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        else:
            if change >= price:
                change -= price
                print(f"Your remaining balance is ₱{change:.2f}.")
            else:
                print("Insufficient balance from your previous payment. Restarting process.")
                cash_rendered = 0

# Start the program
if __name__ == "__main__":
    process_order()
