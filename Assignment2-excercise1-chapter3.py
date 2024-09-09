# Ask for the length of the zander
length = float(input("Enter the length of the zander in centimeters: "))

# Size limit for the zander
size_limit = 42

# Check if the zander is big enough
if length >= size_limit:
    print("The zander meets the size limit. You can keep it!")
else:
    difference = size_limit - length
    print(f"The zander is {difference:.1f} cm below the size limit. Please release it back into the lake.")
