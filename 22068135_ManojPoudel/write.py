import datetime


def purchase_bill(distributor_name, item):
    Company_Name = "Tech Zone"
    Company_Address = "Kamalpokhari,Kathmandu"
    Company_Phone = "01-2596378"
    Company_EMAIL = "techzone.laptopshop@gmail.com"
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


def sold_bill(success, items, Customer_Name):
    Company_Name = "Tech Zone"
    Company_Address = "Kamalpokhari,Kathmandu"
    Company_Phone = "01-2596378"
    Company_EMAIL = "techzone.laptopshop@gmail.com"
    if success or len(items) > 0:
        invoice = (
            f"{Customer_Name}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
            # create invoice name with the distributor name, laptop name, and timestamp
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
