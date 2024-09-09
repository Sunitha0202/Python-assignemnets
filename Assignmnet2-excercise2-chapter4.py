# Define the conversion factor (1 inch = 2.54 centimeters)
conversion_factor = 2.54

# Start an infinite loop
while True:
    # Ask the user for input in inches
    inches = float(input("Enter a value in inches (negative value to quit): "))

    # Check if the input is a negative value
    if inches < 0:
        print("Negative value entered. Program terminated.")
        break  # Exit the loop if negative value is entered

    # Convert inches to centimeters
    centimeters = inches * conversion_factor

    # Print the result
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters.\n")
