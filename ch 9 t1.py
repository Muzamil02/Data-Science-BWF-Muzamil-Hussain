"""Exercise 9.1"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Muxu Paradise", "Asian")      #Instance of Restaurant class

print(restaurant.restaurant_name)                      #Attributes
print(restaurant.cuisine_type)

restaurant.describe_restaurant()                       #Calling methods
restaurant.open_restaurant()