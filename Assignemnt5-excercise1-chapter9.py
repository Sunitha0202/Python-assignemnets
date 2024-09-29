class Car:
    def __init__(self, registration_number, max_speed):
        """Initialize the car with registration number and max speed.
        Set current speed and travelled distance to 0."""
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Create a new car object
my_car = Car("ABC-123", 142)

# Print all properties of the car
print(f"Registration number: {my_car.registration_number}")
print(f"Maximum speed: {my_car.max_speed} km/h")
print(f"Current speed: {my_car.current_speed} km/h")
print(f"Travelled distance: {my_car.travelled_distance} km")
