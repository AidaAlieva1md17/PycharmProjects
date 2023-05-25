class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.name} Кухня: {self.cuisine_type}.")


restaurant1 = Restaurant("France", "French")
restaurant2 = Restaurant("Sushi ", "Japanese")
restaurant3 = Restaurant("Italia", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
