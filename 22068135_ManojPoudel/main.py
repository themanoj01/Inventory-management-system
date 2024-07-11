import read
import operations

"""Displays the laptop details by the function display_laptops(laptops)"""


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


read.read_laptops(read.file)
display_laptops(read.laptops)


def user_option():
    """
    The function first displays the shop information and asks the user to enter their name. Then, it displays the available
    options and prompts the user to select an option by entering a number. The options are:
    - Purchase laptops from manufacturer
    - Sell laptops to customer
    - Display available laptops
    - Exit from system
    """
    print("Shop Name: Tech Zone")
    print("Address: Kamalpokhari,Kathmandu")
    print("Phone No: 01-2596378")
    print("Email: techzone.laptopshop@gmail.com")
    # Shop details print
    #  Welcome message to the User
    user_name = input("Could you please tell us your name? ")
    print("-" * 70 + "\n")
    print(
        f"Greetings, {user_name}! We are delighted to have you in the tech zone. Could you kindly choose from the available options what you would like to accomplish today?"
    )
    print("-" * 70 + "\n")
    ques = True
    while ques:
        try:
            option = int(
                input(
                    "[Please enter 1 to purchase from manufacturer,press 2 to sell to customer,press 3 to display laptops available AND press 4 to exit from system]: "
                )
            )

            if option == 1:
                operations.purchase_laptops()
                ques = True
            elif option == 2:
                operations.sell_to_customer()
                ques = True
            elif option == 3:
                display_laptops(read.laptops)
                ques = True
            elif option == 4:
                print("Thank You for Visiting our store. please Come Again.")
                ques = False
            else:
                print("Invalid option. please choose a valid option.")
                ques = True
        except ValueError:
            print("Invalid input. Please enter a valid option.")


# try except for exception handling if any invalid input appears.

user_option()
