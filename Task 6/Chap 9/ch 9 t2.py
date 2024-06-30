"""Exercise 9.2"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant1 = Restaurant("Muxu Paradise", "Asian")      #Three Instnces of Restaurant class
restaurant2 = Restaurant("Muz World", "Japanese")
restaurant3 = Restaurant("Yango Roast", "Thai")

restaurant1.describe_restaurant()       #Calling methods
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()