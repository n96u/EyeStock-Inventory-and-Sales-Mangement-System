# EyeStock: Sales and Inventory Management System
# Admin Function
def admin(admin_username, admin_password, earnings, capital, stocks):
    # Admin interface for managing capital, purchasing, updating, and removing stocks. 
    print("Welcome to EyeStock Admin!")

    # If capital is zero, prompt the admin to input initial capital
    if capital == 0:
        while True:
            try:
                capital = float(input("Enter capital of EyeStock: "))
                if capital > 0:
                    print("Capital added.")
                    break
                else:
                    print("Insufficient capital. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Display current earnings
    print(f"EyeStock's Earnings: ${earnings:.2f}")

    # Admin menu loop
    while True:
        print("\nSelect purpose:")
        print("1. Purchase Stocks from Manufacturers")
        print("2. Retrieve Available Stocks")
        print("3. Update Stock Prices")
        print("4. Remove Stock")
        print("5. Exit")
        choice = input("Choice: ").strip()

        # Option 1: Purchase stocks
        if choice == "1":
            print("Stock Menu:")
            # Manufacturer stock catalog with default prices
            manufacturer_stocks = {
                "Eyeglass": 120, "Sunglass": 50, "Eye Creamer": 178, "Eye Drops": 49, "Frame": 368,
                "Clear Contact Lens": 149, "Colored Contact Lens": 200, "Lens Solution": 90,
                "Reading Glass": 110, "Cleaning Spray": 30, "Eyewear Case": 120, "Repair Kit": 80,
                "Lens Wipes": 25, "Lens Cloth": 20, "Nose Pad": 35, "Eye Massager": 250,
                "Glass Strap": 25, "Sports Glasses": 190, "Ear Grip Hook": 30, "Anti-Radiation Glasses": 180
            }

            # Assign numbers to each stock for easy selection
            stock_list = list(manufacturer_stocks.items())
            stock_dict = {str(i + 1): stock_list[i][0] for i in range(len(stock_list))}

            # Display available manufacturer stocks
            print("Available stocks from manufacturers:")
            for num, name in stock_dict.items():
                print(f"{num}. {name}: ${manufacturer_stocks[name]}")

            # Loop to allow multiple purchases
            while True:
                stock_num = input("Enter the number of the stock to purchase (or type 'done' to finish): ").strip()
                if stock_num.lower() == "done":
                    break
                if stock_num in stock_dict:
                    stock_name = stock_dict[stock_num]
                    try:
                        quantity = int(input(f"Enter quantity for {stock_name}: "))
                        if quantity <= 0:
                            print("Quantity must be greater than 0.")
                            continue
                        total_cost = manufacturer_stocks[stock_name] * quantity
                        if total_cost <= capital:
                            capital -= total_cost
                            
                            # If stock exists, increase quantity
                            if stock_name in stocks:
                                stocks[stock_name]["quantity"] += quantity
                            else:

                                # Ask for resale price for new stock
                                while True:
                                    try:
                                        resale_price = float(input(f"Enter resale price for {stock_name}: "))
                                        if resale_price > 0:
                                            stocks[stock_name] = {"quantity": quantity, "price": resale_price}
                                            break
                                        else:
                                            print("Resale price must be greater than 0.")
                                    except ValueError:
                                        print("Invalid input. Enter a numeric resale price.")
                            print(f"Purchased {quantity} of {stock_name}. Remaining capital: ${capital:.2f}")
                        else:
                            print("Insufficient capital to purchase this stock.")
                    except ValueError:
                        print("Invalid input. Please enter a valid quantity.")
                else:
                    print("Invalid number. Please select from the available stock list.")

        # Option 2: Retrieve available stocks
        elif choice == "2":
            print("Stocks available in the shop:")
            if stocks:
                for item, details in stocks.items():
                    print(f"{item}: Quantity: {details['quantity']:<5}, Resale Price: ${details['price']:<5.2f}")
            else:
                print("No stocks available.")

        # Option 3: Update resale price of a stock
        elif choice == "3":
            stock_name = input("Enter the stock name to update price: ").strip()
            if stock_name in stocks:
                try:
                    new_price = float(input(f"Enter the new price for {stock_name}: "))
                    if new_price > 0:
                        stocks[stock_name]["price"] = new_price
                        print(f"Updated price for {stock_name} to ${new_price:.2f}")
                    else:
                        print("Price must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid price.")
            else:
                print("Stock not found.")

        # Option 4: Remove a stock item
        elif choice == "4":
            stock_name = input("Enter the stock name to remove: ").strip()
            if stock_name in stocks:
                del stocks[stock_name]
                print(f"Removed {stock_name} from inventory.")
            else:
                print("Stock not found.")

        # Option 5: Exit admin menu
        elif choice == "5":
            print("Exiting admin menu.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    # Returning the updated capital after admin actions
    return capital

# Customer Function
def customer(stocks, earnings, capital):
    print("Welcome to EyeStock Customer Menu!")
    if not stocks:
        print("No stocks available for purchase at the moment.")
        return earnings, capital

    # Cart stores selected items
    cart = {}

    # Customer shopping loop
    while True:
        print("\nAvailable stocks:")
        for item, details in stocks.items():
            print(f"{item}: Quantity: {details['quantity']:<5}, Price: ${details['price']:<5.2f}")
        
        stock_name = input("Enter the stock name to purchase (or type 'done' to finish): ").strip()
        if stock_name.lower() == "done":
            break
        if stock_name in stocks:
            try:
                quantity = int(input(f"Enter quantity for {stock_name}: "))
                if 0 < quantity <= stocks[stock_name]["quantity"]:

                    # Add to cart
                    if stock_name in cart:
                        cart[stock_name]["quantity"] += quantity
                    else:
                        cart[stock_name] = {"quantity": quantity, "price": stocks[stock_name]["price"]}
                    stocks[stock_name]["quantity"] -= quantity
                    print(f"Added {quantity} of {stock_name} to your cart.")
                else:
                    print("Invalid quantity. Please enter a valid amount within stock limits.")
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")
        else:
            print("Invalid stock name. Please select from the available stocks.")

    # Process payment if cart is not empty
    if cart:
        print("\nGenerating receipt...")
        total_cost = 0
        print("Receipt:")
        print("-" * 30)
        for item, details in cart.items():
            item_cost = details["quantity"] * details["price"]
            total_cost += item_cost
            print(f"{item}: Quantity: {details['quantity']}, Price: ${details['price']:.2f}, Total: ${item_cost:.2f}")
        print("-" * 30)
        print(f"Total Cost: ${total_cost:.2f}")
        
        # Handle payment
        while True:
            try:
                amount = float(input(f"Enter the total amount you want to pay (Total: ${total_cost:.2f}): "))
                if amount >= total_cost:
                    change = amount - total_cost
                    print(f"Payment of ${amount:.2f} received. Change: ${change:.2f}")
                    earnings += total_cost
                    capital += total_cost  # Add the earnings to capital after a customer purchase
                    print("Thank you for your purchase!")
                    break
                else:
                    print(f"Insufficient payment. You need to pay at least ${total_cost:.2f}.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
    else:
        print("No items purchased.")

    # Returning updated earnings and capital
    return earnings, capital

# Main Function
def main(admin_username, admin_password, earnings, capital, stocks):
    print("EyeStock: Sales and Inventory Management System")
    while True:
        choice = input("Please select one of the following options\n1. Admin\n2. Customer\n3. Exit\nChoice: ").strip()

        # Admin login
        if choice == "1":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            if username == admin_username and password == admin_password:
                print("Login successful.")
                capital = admin(admin_username, admin_password, earnings, capital, stocks)
            else:
                print("Invalid username or password.")
        
        # Customer interface
        elif choice == "2":
            earnings, capital = customer(stocks, earnings, capital)
        
        # Exit the system
        elif choice == "3":
            print("Have a nice day!")
            break
        else:
            print("Invalid input. Please enter the number of your choice.")

# Program entry point
if __name__ == "__main__":
    # Initial call to main with default credentials and values
    main("admin", "admin123", 0.0, 0.0, {})