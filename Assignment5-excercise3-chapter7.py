# Dictionary to store airport data (ICAO code as key, airport name as value)
airport_data = {}


def add_airport():
    """Function to add a new airport to the dictionary"""
    icao_code = input("Enter the ICAO code of the airport: ").upper()
    airport_name = input("Enter the name of the airport: ")
    if icao_code in airport_data:
        print(f"Airport with ICAO code {icao_code} already exists!")
    else:
        airport_data[icao_code] = airport_name
        print(f"Airport {airport_name} added successfully with ICAO code {icao_code}.")


def fetch_airport():
    """Function to fetch the airport name by ICAO code"""
    icao_code = input("Enter the ICAO code of the airport to fetch: ").upper()
    if icao_code in airport_data:
        print(f"The name of the airport with ICAO code {icao_code} is {airport_data[icao_code]}.")
    else:
        print(f"No airport found with ICAO code {icao_code}.")


# Main loop to run the program
while True:
    print("\nChoose an option:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_airport()
    elif choice == '2':
        fetch_airport()
    elif choice == '3':
        print("Quitting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
