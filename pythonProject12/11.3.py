class Restaurant:
    def __init__(self, name, cuisine_type, rating):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.name} Кухня: {self.cuisine_type}. Рейтинг: {self.rating}")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Название ресторана: {self.name} Кухня: {self.cuisine_type}.Рейтинг обновлен: {self.rating}")
        print(f"Название ресторана: {self.name} Кухня: {self.cuisine_type}. Обновленный рейтинг: {self.rating}")


restaurant1 = Restaurant("France", "French", 4.5)
restaurant1.describe_restaurant()
restaurant1.update_rating(4.7)