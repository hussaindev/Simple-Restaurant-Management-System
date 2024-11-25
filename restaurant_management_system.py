# Restaurant Management System

# Menu Dictionary
menu = {
    "Burger": 4.99,
    "Pizza": 6.99,
    "Fries": 1.5,
    "Coke": 1
}

# Display Menu
def display_menu(menu):
    print("Menu List:")
    for item, price in menu.items():
        print(f"{item} - ${price:.2f}")
    print("\nOffers Available!\n"
          "- If you spend over $50: Get 10% off\n"
          "- If you spend over $70: Get 17% off\n"
          "- If you spend over $100: Get 20% off\n"
          "Happy Meal!\n")

# Take Customer Order
def take_order(menu):
    order = []
    while True:
        item = input("Enter an item to order (or 'done' to finish): ").title()
        if item == "Done":
            break
        elif item in menu:
            try:
                quantity = int(input(f"Enter quantity for {item}: "))
                if quantity > 0:
                    order.append((item, quantity))
                else:
                    print("Quantity must be greater than 0.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print(f"'{item}' is not available. Please choose from the menu.")
    return order

# Calculate Bill with Discounts
def calculate_bill(order, menu):
    total = sum(menu[item] * quantity for item, quantity in order)
    discount_rate = 0
    
    # Apply discounts
    if 50 < total <= 70:
        discount_rate = 0.10
    elif 70 < total <= 100:
        discount_rate = 0.17
    elif total > 100:
        discount_rate = 0.20

    discount = total * discount_rate
    final_total = total - discount

    print("\n--- Bill Summary ---")
    for item, quantity in order:
        print(f"{item} x {quantity} = ${menu[item] * quantity:.2f}")
    print(f"Subtotal: ${total:.2f}")
    if discount_rate > 0:
        print(f"Discount ({int(discount_rate * 100)}%): -${discount:.2f}")
    print(f"Total: ${final_total:.2f}\n")
    
    return final_total

# Collect Customer Feedback
def collect_feedback():
    name = input("Please enter your name: ").title()
    feedback = input(f"Hi {name}, please share your feedback: ")
    return name, feedback

# Main Program
def main():
    display_menu(menu)
    order = take_order(menu)
    if order:
        final_bill = calculate_bill(order, menu)
        print(f"Thank you for your order! Your final bill is: ${final_bill:.2f}")
    else:
        print("No items were ordered.")

    name, feedback = collect_feedback()
    print(f"Thank you, {name}, for your feedback: '{feedback}'")

if __name__ == "__main__":
    main()