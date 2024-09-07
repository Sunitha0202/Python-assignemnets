# Conversion constants
LOT_TO_GRAMS = 13.3
POUND_TO_LOTS = 32
TALENT_TO_POUNDS = 20

# Ask the user for input in medieval units
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# Convert everything to grams
total_lots = (talents * TALENT_TO_POUNDS * POUND_TO_LOTS) + (pounds * POUND_TO_LOTS) + lots
total_grams = total_lots * LOT_TO_GRAMS

# Convert grams to kilograms and remaining grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

# Display the result
print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")
