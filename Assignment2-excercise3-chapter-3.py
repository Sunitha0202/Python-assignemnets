# Ask the user for biological gender and hemoglobin value
gender = input("Enter your biological gender (male/female): ").lower()
hemoglobin = float(input("Enter your hemoglobin value (g/l): "))

# Check the hemoglobin value for females
if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin value is low.")
    elif 117 <= hemoglobin <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")

# Check the hemoglobin value for males
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin value is low.")
    elif 134 <= hemoglobin <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")

# Handle invalid gender input
else:
    print("Invalid gender entered.")
