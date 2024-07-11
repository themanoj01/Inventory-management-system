file = "Main.txt"
# Define the list to store the laptop information
laptops = []

"""This function is for reading contents of main text file and append those details in a list called 'laptops' """


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
