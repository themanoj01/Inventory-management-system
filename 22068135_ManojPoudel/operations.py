import write


def purchase_laptops():
    distributor_name = input("Enter the Name of distributor: ")
    more = True
    price = True
    quantity = True
    item = []
    while more:
        try:
            Name = input("Enter the name of laptop: ")
            Brand = input("Enter the brand of laptop: ")
            # checking if the price entered is valid
            while price:
                try:
                    Price = int(input("Enter the price of the laptop: "))
                    if Price > 0:
                        break
                    else:
                        print("***Invalid Price***")
                        price = True
                except ValueError:
                    print("Please enter a valid integer for the price.")
                    # quantity check if valid or not
            while quantity:
                try:
                    Quantity = int(input("Enter the quantity to be ordered: "))
                    if Quantity > 0:
                        break
                    else:
                        print("***Invalid Quantity***")
                        quantity = True
                except ValueError:
                    print("Please enter a valid integer for the quantity.")
            """Calculation for billing"""
            Net_amount = Price * Quantity
            VAT_RATE = 13 / 100
            Vat_amount = Net_amount * VAT_RATE
            Gross_amount = Net_amount + Vat_amount
            # Appending the purchase details in a list called item
            item.append(
                [
                    Name,
                    Brand,
                    Price,
                    Quantity,
                    distributor_name,
                    Net_amount,
                    Vat_amount,
                    Gross_amount,
                ]
            )
        except ValueError:
            print("Invalid input value. Please enter a valid integer.")

            # Ask if the user wants to add more laptops
        add = True
        while add:
            add_more = input(
                "Do you want to add more laptops to the same invoice? (Y/N) :"
            ).lower()
            if add_more == "y":
                more = True
                break
            elif add_more == "n":
                print("Exiting from the purchase system.")
                add = False
                more = False
            else:
                print("Please try again with a valid input('y' or 'n')")
                add = True
        with open("Main.txt", "r") as file:
            laptops = file.readlines()
            """ code to update stock from main text file"""
        updated_stock = []
        for line in laptops:
            laptop_details = line.strip().split(",")
            if laptop_details[0] == Name and laptop_details[1] == Brand:
                laptop_details[3] = str(int(laptop_details[3]) + Quantity)
                updated_line = ",".join(laptop_details) + "\n"
                updated_stock.append(updated_line)
                print(
                    f"The stock of {Quantity} {Brand} {Name} laptop(s) has been updated."
                )

            else:
                updated_line = line
                updated_stock.append(updated_line)
            updated_stocks = "".join(updated_stock)
            with open("Main.txt", "w") as file:
                file.write(updated_stocks)
    # Calling billing function when purchase process completed
    write.purchase_bill(distributor_name, item)


def sell_to_customer():
    Customer_Name = input("Enter the name of Customer: ")
    more = True
    quantity = True
    shipping_cost = 0
    items = []
    success = True  # keep track of whether all requested laptops were sold successfully
    found_laptop = False
    # keeping track of if laptop matching name and brand found or not
    while more:
        Name = input("Enter the name of the laptop you want to buy:")
        Brand = input("Enter the brand of laptop you want to buy: ")
        while quantity:
            try:
                Quantity = int(input("Enter the quantity you need: "))
                # Checking quantity validation
                if Quantity > 0:
                    break
                else:
                    print("***invalid quantity***")
                    quantity = True
            except ValueError:
                print("Invalid input. Please enter a valid integer for the quantity.")
        with open("Main.txt", "r") as file:
            laptops = file.readlines()

        for line in laptops:
            laptop_details = line.strip().split(",")
            if laptop_details[0] == Name and laptop_details[1] == Brand:
                print(f"{Name} {Brand} found in the stock.")
                found_laptop = True
                if int(laptop_details[3]) >= Quantity:
                    print(
                        f"The stock of {Quantity} {Brand} {Name} laptop(s) has been updated."
                    )
                    # Asking user if they want their product to be shipped or not
                    ship = True
                    while ship:
                        shipping = input(
                            "Do you want your product to be shipped? (Y/N) : "
                        )

                        if shipping.lower() == "y":
                            shipping_cost = 100
                            break
                        elif shipping.lower() == "n":
                            shipping_cost = 0
                            break
                        else:
                            print(
                                "Please try again with a valid input. Answer only with 'y' or 'n'."
                            )
                            ship = True
                else:
                    print(
                        f"Error: Sorry, Not enough {Name} {Brand} laptops in stock to sell."
                    )
                # Asking user if they want to add laptops to the same invoice
        if not found_laptop:
            print(
                f"Error: Sorry,{Name} {Brand} laptop is not available with us. You can have a look on other products if interested otherwise you may exit the system."
            )
        success = False
        add = True
        while add:
            add_more = input("Do you want to add more laptops ? (Y/N) :").lower()
            if add_more == "y":
                more = True
                break

            elif add_more == "n":
                print("Exiting from the purchase system.")
                add = False
                more = False

            else:
                print("Please try again with a valid input.Answer with 'y' or 'n'.")
                add = True

        with open("Main.txt", "r") as file:
            laptops = file.readlines()
            # Updating main text file
        updated_stock = []
        for line in laptops:
            laptop_details = line.strip().split(",")
            if laptop_details[0] == Name and laptop_details[1] == Brand:
                if int(laptop_details[3]) >= Quantity:
                    laptop_details[3] = str(int(laptop_details[3]) - Quantity)
                    Amount = int(laptop_details[2].replace("$", "")) * Quantity
                    Total_Amount_to_be_paid = Amount + shipping_cost
                    #  Adding sold items details to list items which we need for billing
                    items.append(
                        [
                            Name,
                            Brand,
                            Quantity,
                            Customer_Name,
                            Amount,
                            shipping_cost,
                            Total_Amount_to_be_paid,
                        ]
                    )
                else:
                    success = False
            updated_stock.append(",".join(laptop_details))
        updated_stocks = "\n".join(updated_stock)
        try:
            with open("Main.txt", "w") as file:
                file.write(updated_stocks)
        except Exception as e:
            print("Error updating stock file:", e)
    # Calling bill function after selling process completion
    write.sold_bill(success, items, Customer_Name)
