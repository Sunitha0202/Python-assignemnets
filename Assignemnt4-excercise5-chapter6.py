# Function to remove odd numbers from the list
def remove_odd_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


# Main program
def main():
    # Create a list of integers
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Call the function to get a list with only even numbers
    filtered_list = remove_odd_numbers(original_list)

    # Print both the original list and the filtered list
    print("Original list:", original_list)
    print("Filtered list (even numbers only):", filtered_list)


# Call the main function
main()