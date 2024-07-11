import datetime

file = "Main.txt"
# Define the list to store the laptop information
laptops = []

def read_laptops(file):
    try:
        # Open the file in read mode
        with open("Main.txt", "r") as file:
            for line in file:
                laptop_details = line.strip().split(",")
                if len(laptop_details) == 8:  # check if there are enough elements
                    # Create a list to store the laptop information
                    laptop_list = [
                        laptop_details[0],
                        laptop_details[1],
                        int(laptop_details[2].replace("$", "")),
                        laptop_details[3],
                        laptop_details[4],
                        laptop_details[5],
                        laptop_details[6],
                        laptop_details[7],
                    ]
                    # Add the laptop information to the list
                    laptops.append(laptop_list)
        return laptops
    except FileNotFoundError:
        print("The file could not be found.")


# print(laptops)


def display_laptops(laptops):
    # Print table header
    print(
        "+----------------------------------------------------------------------------------------------------------------------------------------+"
    )
    print(
        "| {:<20} | {:<12} | {:<10} | {:<6} | {:<21} | {:<24} | {:<9} | {:<5} | ".format(
            "Name",
            "Brand",
            "Price($)",
            "Quantity",
            "Processor",
            "Graphics Card",
            "Warranty",
            "RAM",
        )
    )
    print(
        "+----------------------------------------------------------------------------------------------------------------------------------------+"
    )
    # Print each row of laptop data
    for laptop in laptops:
        print(
            "| {:<20} | {:<12} | ${:<10} | {:<6} | {:<21} | {:<24} | {:<9} | {:<5} ".format(
                laptop[0],
                laptop[1],
                laptop[2],
                laptop[3],
                laptop[4],
                laptop[5],
                laptop[6],
                laptop[7],
            )
        )
        print(
            "+--------------------------------------------------------------------------------------------------------------------------------------+"
        )


read_laptops(file)
display_laptops(laptops)

Company_Name = "Tech Zone"
Company_Address = "Kamalpokhari,Kathmandu"
Company_Phone = "01-2596378"
Company_EMAIL = "techzone.laptopshop@gmail.com"


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

            Net_amount = Price * Quantity
            VAT_RATE = 13 / 100
            Vat_amount = Net_amount * VAT_RATE
            Gross_amount = Net_amount + Vat_amount

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
    purchase_bill(distributor_name, item)
            # create invoice name with the distributor name, laptop name, and timestamp


def purchase_bill(distributor_name, item):
    invoice = (
        f"{distributor_name}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    )
    with open(invoice, "w") as bill:
        # Company information section

        bill.write("=" * 60 + "\n")
        bill.write("\t" "***Welcome to the tech Zone.***\n")
        bill.write("\t\t" f"{Company_Name}\n")
        bill.write("\t\t" f"{Company_Address}\n\n")
        bill.write("\t\t" f"Phone: {Company_Phone}\n")
        bill.write("\t\t" f"Email: {Company_EMAIL}\n\n")

        # Invoice details section
        bill.write("=" * 60 + "\n\n")
        bill.write("Invoice detail: " + invoice + "\n")
        bill.write(
            "Date and Time of transaction: "
            + str({datetime.datetime.now().strftime("%Y/%m/%d %H-%M-%S")})
            + "\n"
        )
        bill.write(f"Distributor: {distributor_name}\n\n")
        for i in range(0, len(item)):
            # Laptop details section
            bill.write("=" * 60 + "\n\n")
            bill.write("LAPTOP INFORMATION\n")
            bill.write("=" * 20 + "\n")
            bill.write(f"Laptop:\t\t{item[i][0]}\n")
            bill.write(f"Brand:\t\t{item[i][1]}\n")
            bill.write(f"Quantity:\t{item[i][3]}\n\n")

            # Price details section
            # bill.write('=' * 60 + "\n\n")
            bill.write("PRICE DETAILS\n")
            bill.write("=" * 20 + "\n")
            bill.write(f"Price:\t\t${item[i][2]}\n")
            bill.write(f"Net amount:\t\t${item[i][5]:.2f}\n")
            bill.write(f"VAT Amount:\t\t${item[i][6]:.2f}\n")
            bill.write(f"Gross amount:\t\t${item[i][7]:.2f}\n\n")

        # Thank you message
        bill.write("*" * 60 + "\n")
        bill.write("Thank you for the business!\n")
        bill.write("Hoping to work with you again in the future.\n")
        bill.write("*" * 60 + "\n")
    print(f"Selected Laptops ordered successfully. Invoice is saved in {invoice}.")

    # printing bill in console.
    with open(invoice, "r") as bill:
        details = bill.read()
        print(details)


def sell_to_customer():
    Customer_Name = input("Enter the name of Customer: ")
    more = True
    quantity = True
    shipping_cost = 0
    items = []
    success = True  # keep track of whether all requested laptops were sold successfully

    while more:
        Name = input("Enter the name of the laptop you want to buy:")
        Brand = input("Enter the brand of laptop you want to buy: ")
        while quantity:
            try:
                Quantity = int(input("Enter the quantity you need: "))

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
                if int(laptop_details[3]) >= Quantity:
                    print(
                        f"The stock of {Quantity} {Brand} {Name} laptop(s) has been updated."
                    )
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
        updated_stock = []
        for line in laptops:
            laptop_details = line.strip().split(",")
            if laptop_details[0] == Name and laptop_details[1] == Brand:
                if int(laptop_details[3]) >= Quantity:
                    laptop_details[3] = str(int(laptop_details[3]) - Quantity)
                    Amount = int(laptop_details[2].replace("$", "")) * Quantity
                    Total_Amount_to_be_paid = Amount + shipping_cost
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
    sold_bill(success, items, Customer_Name)

def sold_bill(success, items, Customer_Name):
    if success or len(items) > 0:
        invoice = (
            f"{Customer_Name}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        )
        with open(invoice, "w") as bill:
            # Company information section

            bill.write("=" * 60 + "\n")
            bill.write("\t" "***Welcome to the tech Zone.***\n")
            bill.write("\t\t" f"{Company_Name}\n")
            bill.write("\t\t" f"{Company_Address}\n\n")
            bill.write("\t\t" f"Phone: {Company_Phone}\n")
            bill.write("\t\t" f"Email: {Company_EMAIL}\n\n")

            # Invoice details section
            bill.write("=" * 60 + "\n\n")
            bill.write("Invoice detail: " + invoice + "\n")
            bill.write(
                "Date and Time of transaction: "
                + str({datetime.datetime.now().strftime("%Y/%m/%d %H-%M-%S")})
                + "\n"
            )
            bill.write(f"Customer's Name: {Customer_Name}\n\n")

            # Laptop details section
            for i in range(0, len(items)):
                # items.append(','.join())
                bill.write("=" * 60 + "\n\n")
                bill.write("LAPTOP INFORMATION\n")
                bill.write("=" * 20 + "\n")
                bill.write(f"Laptop:\t\t{items[i][0]}\n")
                bill.write(f"Brand:\t\t{items[i][1]}\n")
                bill.write(f"Quantity:\t{items[i][2]}\n\n")

                # Price details section
                # bill.write('=' * 60 + "\n\n")
                bill.write("PRICE DETAILS\n")
                bill.write("=" * 20 + "\n")
                bill.write(f"Amount:\t\t\t\t\t${items[i][4]:.2f}\n")
                bill.write(f"Shipping_Cost:\t\t\t\t${items[i][5]:.2f}\n")
                bill.write(f"Total_Amount_to_be_paid :\t${items[i][6]:.2f}\n\n")

            # Thank you message
            bill.write("*" * 60 + "\n")
            bill.write("Thank you for the business!\n")
            bill.write("Hoping to work with you again in the future.\n")
            bill.write("*" * 60 + "\n")
        print(
            f" Invoice of successfully sold laptops with details is saved in {invoice}."
        )

        # printing bill in console.
        with open(invoice, "r") as bill:
            details = bill.read()
            print(details)


# Asking User if they want to purchase, sell laptops or display available laptops.
def user_option():
    print("Shop Name: Tech Zone")
    print("Address: Kamalpokhari,Kathmandu")
    print("Phone No: 01-2596378")
    print("Email: techzone.laptopshop@gmail.com")
    user_name = input("Could you please tell us your name? ")
    print("-" * 70 + "\n")
    print(
        f"Greetings, {user_name}! We are delighted to have you in the tech zone. Could you kindly choose from the available options what you would like to accomplish today?"
    )
    print("-" * 70 + "\n")
    read_laptops(laptops)
    ques = True
    while ques:
        try:
            option = int(
                input(
                    "[Please enter 1 to purchase from manufacturer,press 2 to sell to customer,press 3 to display laptops available AND press 4 to exit from system]: "
                )
            )

            if option == 1:
                purchase_laptops()
                ques = True
            elif option == 2:
                sell_to_customer()
                ques = True
            elif option == 3:
                display_laptops(laptops)
                ques = True
            elif option == 4:
                print("Thank You for Visiting our store. please Come Again.")
                ques = False
            else:
                print("Invalid option. please choose a valid option.")
                ques = True
        except ValueError:
            print("Invalid input. Please enter a valid option.")


user_option()
