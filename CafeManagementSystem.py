import datetime

# Initial Menu
menu = {
    1: {"name": "Coffee", "price": 80},
    2: {"name": "Tea", "price": 40},
    3: {"name": "Cold Coffee", "price": 120},
    4: {"name": "Burger", "price": 100},
    5: {"name": "Pizza", "price": 180},
    6: {"name": "Sandwich", "price": 90},
    7: {"name": "French Fries", "price": 80},
    8: {"name": "Pasta", "price": 150},
    9: {"name": "Ice Cream", "price": 70}
}

# Admin Credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

# Global Variables
total_sales = 0
order_number = 1


# Display Menu
def display_menu():

    print("\n========== CAFE MENU ==========")
    print("ID\tItem\t\tPrice")
    print("--------------------------------")

    if not menu:
        print("No items available.")
        return

    for item_id, item in menu.items():
        print(f"{item_id}\t{item['name']:<15} Rs.{item['price']}")

    print("--------------------------------")


# Admin Login
def admin_login():

    print("\n========== ADMIN LOGIN ==========")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("\nAdmin Login Successful!")
        return True

    print("\nInvalid Username or Password!")
    return False


# Add Menu Item
def add_menu_item():

    try:
        item_id = int(input("Enter New Item ID: "))

        if item_id <= 0 or item_id in menu:
            print("Invalid or Existing Item ID!")
            return

        name = input("Enter Item Name: ").strip()
        price = float(input("Enter Item Price: "))

        if not name or price <= 0:
            print("Invalid Item Details!")
            return

        menu[item_id] = {
            "name": name,
            "price": price
        }

        print("Item Added Successfully!")

    except ValueError:
        print("Invalid Input!")


# Update Menu Item
def update_menu_item():

    display_menu()

    try:
        item_id = int(input("Enter Item ID to Update: "))

        if item_id not in menu:
            print("Item Not Found!")
            return

        print("1. Update Name")
        print("2. Update Price")
        print("3. Update Both")

        choice = int(input("Enter Choice: "))

        if choice not in [1, 2, 3]:
            print("Invalid Choice!")
            return

        new_name = menu[item_id]["name"]
        new_price = menu[item_id]["price"]

        if choice in [1, 3]:
            new_name = input("Enter New Name: ").strip()

            if not new_name:
                print("Name cannot be empty!")
                return

        if choice in [2, 3]:
            new_price = float(input("Enter New Price: "))

            if new_price <= 0:
                print("Price must be greater than zero!")
                return

        menu[item_id]["name"] = new_name
        menu[item_id]["price"] = new_price

        print("Item Updated Successfully!")

    except ValueError:
        print("Invalid Input!")


# Delete Menu Item
def delete_menu_item():

    display_menu()

    try:
        item_id = int(input("Enter Item ID to Delete: "))

        if item_id not in menu:
            print("Item Not Found!")
            return

        confirm = input("Confirm Delete? (yes/no): ").lower()

        if confirm == "yes":
            del menu[item_id]
            print("Item Deleted Successfully!")
        else:
            print("Deletion Cancelled!")

    except ValueError:
        print("Invalid Input!")


# Admin Panel
def admin_panel():

    if not admin_login():
        return

    while True:

        print("\n========== ADMIN PANEL ==========")
        print("1. Display Menu")
        print("2. Add New Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. View Sales")
        print("6. Logout")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                display_menu()

            elif choice == 2:
                add_menu_item()

            elif choice == 3:
                update_menu_item()

            elif choice == 4:
                delete_menu_item()

            elif choice == 5:
                print("\nTotal Sales: Rs.", total_sales)

            elif choice == 6:
                print("Admin Logged Out!")
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Enter a Valid Number!")


# Customer Section
def customer_section():

    global total_sales, order_number

    if not menu:
        print("Sorry! No Menu Items Available.")
        return

    customer_name = input("\nEnter Customer Name: ").strip()

    if not customer_name:
        print("Customer name cannot be empty!")
        return

    order = []

    while True:

        display_menu()

        try:
            item_id = int(input("Enter Item ID (0 to Finish): "))

            if item_id == 0:
                break

            if item_id not in menu:
                print("Invalid Item ID!")
                continue

            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero!")
                continue

            item = menu[item_id]

            amount = item["price"] * quantity

            order.append({
                "name": item["name"],
                "price": item["price"],
                "quantity": quantity,
                "amount": amount
            })

            print(item["name"], "Added to Order!")

        except ValueError:
            print("Please Enter Valid Numbers!")

    if not order:
        print("No Items Ordered!")
        return

    # Calculate Bill
    subtotal = sum(item["amount"] for item in order)

    discount = 0

    if subtotal >= 1000:
        discount = subtotal * 0.10

    final_amount = subtotal - discount

    # Payment Method
    print("\n========== PAYMENT METHOD ==========")
    print("1. Cash")
    print("2. UPI")
    print("3. Debit/Credit Card")

    while True:

        try:
            payment_choice = int(input("Select Payment Method: "))

            if payment_choice == 1:
                payment_method = "Cash"
                break

            elif payment_choice == 2:
                payment_method = "UPI"
                break

            elif payment_choice == 3:
                payment_method = "Debit/Credit Card"
                break

            else:
                print("Invalid Payment Choice!")

        except ValueError:
            print("Enter a Valid Number!")

    # Display Final Bill
    print("\n")
    print("==============================================")
    print("              CAFE MANAGEMENT SYSTEM")
    print("                  CUSTOMER BILL")
    print("==============================================")

    print("Order Number:", order_number)
    print("Customer Name:", customer_name)

    print(
        "Date:",
        datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    )

    print("----------------------------------------------")

    print(f"{'Item':<15}{'Qty':<5}{'Price':<8}{'Amount'}")

    print("----------------------------------------------")

    for item in order:

        print(
            f"{item['name']:<15}"
            f"{item['quantity']:<5}"
            f"{item['price']:<8}"
            f"{item['amount']:.2f}"
        )

    print("----------------------------------------------")

    print(f"Subtotal:              Rs.{subtotal:.2f}")
    print(f"Discount:              Rs.{discount:.2f}")
    print(f"Final Amount:          Rs.{final_amount:.2f}")

    print("----------------------------------------------")

    print("Payment Method:", payment_method)
    print("Payment Status: Successful")

    print("==============================================")
    print("       THANK YOU FOR VISITING OUR CAFE!")
    print("==============================================")

    # Update Sales
    total_sales += final_amount

    order_number += 1


# Main Program
def main():

    while True:

        print("\n")
        print("**************************************")
        print("        WELCOME TO OUR CAFE")
        print("**************************************")

        print("1. Admin")
        print("2. Customer")
        print("3. Exit")

        print("**************************************")

        try:
            choice = int(input("Are You Admin or Customer? "))

            if choice == 1:
                admin_panel()

            elif choice == 2:
                customer_section()

            elif choice == 3:
                print("Thank You! Visit Again.")
                break

            else:
                print("Invalid Choice! Select 1, 2 or 3.")

        except ValueError:
            print("Please Enter a Valid Number!")


# Start Application
main()
