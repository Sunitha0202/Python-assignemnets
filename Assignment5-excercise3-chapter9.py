class Car:
    def __init__(self, registration_number, max_speed):
        """Initialize the car with registration number and max speed.
        Set current speed and travelled distance to 0."""
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        """Change the speed of the car by the specified amount,
        ensuring it stays within the allowed limits."""
        new_speed = self.current_speed + change

        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        """Increase the travelled distance based on the current speed
        and the number of hours driven."""
        distance = self.current_speed * hours
        self.travelled_distance += distance


# Create a new car object
my_car = Car("ABC-123", 142)

# Increase the speed of the car
my_car.accelerate(30)  # Increase speed by 30 km/h
my_car.accelerate(70)  # Increase speed by 70 km/h
my_car.accelerate(50)  # Attempt to increase speed by 50 km/h

# Print the current speed of the car
print(f"Current speed after acceleration: {my_car.current_speed} km/h")

# Drive the car for 1.5 hours
my_car.drive(1.5)  # Increase travelled distance

# Print the travelled distance
print(f"Travelled distance after driving for 1.5 hours: {my_car.travelled_distance} km")

# Use emergency brake to decrease speed
my_car.accelerate(-200)  # Decrease speed by 200 km/h

# Print the final speed of the car
print(f"Final speed after emergency brake: {my_car.current_speed} km/h")

# Drive the car for another 2 hours
my_car.drive(2)  # Increase travelled distance again

# Print the updated travelled distance
print(f"Travelled distance after driving for 2 hours: {my_car.travelled_distance} km")
