import math


# Function to calculate unit price per square meter
def calculate_unit_price(diameter, price):
    # Calculate the area of the pizza (Area = π * (radius^2))
    radius = diameter / 2
    area_square_meters = math.pi * (radius / 100) ** 2  # Convert cm to meters
    # Calculate the unit price per square meter
    unit_price = price / area_square_meters
    return unit_price


# Main program
def main():
    # Ask for the diameter and price of the first pizza
    diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
    price1 = float(input("Enter the price of the first pizza (in euros): "))

    # Ask for the diameter and price of the second pizza
    diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
    price2 = float(input("Enter the price of the second pizza (in euros): "))

    # Calculate the unit price for both pizzas
    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    # Print out the unit prices
    print(f"Unit price of the first pizza: {unit_price1:.2f} euros/m²")
    print(f"Unit price of the second pizza: {unit_price2:.2f} euros/m²")

    # Determine which pizza is a better value
    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


# Call the main function
main()