def login_system():
    # Define the correct username and password
    correct_username = "python"
    correct_password = "rules"

    # Set a maximum number of allowed attempts
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        # Ask for username and password
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if the entered credentials are correct
        if username == correct_username and password == correct_password:
            print("Welcome!")
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"Incorrect username or password. {remaining_attempts} attempts left.")

        # Check if the user has reached the maximum number of failed attempts
        if attempts == max_attempts:
            print("Access denied.")


# Run the login system
login_system()
