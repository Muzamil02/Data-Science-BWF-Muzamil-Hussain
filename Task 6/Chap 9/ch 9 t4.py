class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value of 0

    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else:
            print("Number served can't be negative!")

    def increment_number_served(self, increment):
        if increment >= 0:
            self.number_served += increment
        else:
            print("Increment can't be negative!")

restaurant = Restaurant("Muxu Paradise", "Asian")

print(restaurant.name)                      #Attributes
print(restaurant.cuisine_type)

restaurant.describe_restaurant()                       #Calling methods
restaurant.open_restaurant()

print(f"Number of customers served: {restaurant.number_served}")

restaurant.number_served = 11
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(26)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(14)
print(f"Number of customers served: {restaurant.number_served}")
