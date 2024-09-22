# Function to convert gallons to liters
def gallons_to_liters(gallons):
    return gallons * 3.78541


# Main program
def main():
    while True:
        # Ask the user for the quantity of gasoline in gallons
        gallons = float(input("Enter quantity of gasoline in American gallons (or a negative value to stop): "))

        # Stop the loop if the input is negative
        if gallons < 0:
            print("Conversion ended.")
            break

        # Convert gallons to liters and display the result
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is {liters:.2f} liters.")


# Call the main function
main()