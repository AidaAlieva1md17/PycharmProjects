class Restaurant:
    def __init__(self, name, cuisine_type, rating):#Определение метода init, который инициализирует атрибуты объекта name, cuisine_type, rating.
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):# Определение метода describe_restaurant, который выводит информацию о ресторане (название, тип кухни и рейтинг).
        print(f"Название ресторана: {self.name} Кухня: {self.cuisine_type}. Рейтинг: {self.rating}")

    def update_rating(self, new_rating):#Определение метода update_rating, который обновляет рейтинг ресторана и выводит информацию об обновлении.
        self.rating = new_rating
        print(f"Название ресторана: {self.name} Кухня: {self.cuisine_type}.Рейтинг обновлен: {self.rating}")
        print(f"Название ресторана: {self.name} Кухня: {self.cuisine_type}. Обновленный рейтинг: {self.rating}")


restaurant1 = Restaurant("France", "French", 4.5)#Создание объекта restaurant1 класса Restaurant с аргументами "France", "French", 4.5.
restaurant1.describe_restaurant()#Вызов метода describe_restaurant() у объекта restaurant1, который выводит информацию о ресторане.
restaurant1.update_rating(4.7)# Вызов метода update_rating() у объекта restaurant1 с аргументом 4.7, который обновляет рейтинг и выводит информацию об обновлении.
class IceCreamStand(Restaurant):#Создан класс "IceCreamStand", наследующийся от класса "Restaurant"
    def __init__(self, name, cuisine_type, rating, flavors, location, working_hours):
        super().__init__(name, cuisine_type, rating)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours

    def show_flavors(self):
        print(f"Список сортов мороженого: {', '.join(self.flavors)}")

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        self.flavors.remove(flavor)

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"{flavor} есть в наличии")
        else:
            print(f"{flavor} нет в наличии")

class StickIceCream(IceCreamStand):
    def __init__(self, name, cuisine_type, rating, flavors, location, working_hours):
        super().__init__(name, cuisine_type, rating, flavors, location, working_hours)
        self.type = "Мороженое на палочке"

    def show_type(self):
        print(f"Тип мороженого: {self.type}")

class IceCream(IceCreamStand):
    def __init__(self, name, cuisine_type, rating, flavors, location, working_hours):
        super().__init__(name, cuisine_type, rating, flavors, location, working_hours)
        self.type = "Мягкое мороженое"

    def show_type(self):
        print(f"Тип мороженого: {self.type}")

