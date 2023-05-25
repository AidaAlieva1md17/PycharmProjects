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
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, rating, flavors):#инициализируеv свойства объекта (название ресторана, тип кухни, рейтинг и список вкусов мороженого)
        super().__init__(name, cuisine_type, rating)#вызываем метод из родительского класса
        self.flavors = flavors

    def show_flavors(self):#выводит список вкусов мороженого
        print("Вкусы мороженного:")
        for flavor in self.flavors:
            print("- " + flavor)


ice_cream_stand = IceCreamStand("Морожняя", "Ice Cream", 4.3, ["Ванильный", "Шоколадный", "Клубничыный"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()
class IceCreamStand(Restaurant):#Создан класс "IceCreamStand", наследующийся от класса "Restaurant"
    def __init__(self, name, cuisine_type, rating, flavors, location, working_hours):
        super().__init__(name, cuisine_type, rating)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours
    def show_flavors(self):
        print(f"Список сортов мороженого: {', '.join(self.flavors)}")

    def add_flavor(self):
        flavor=self.flavors
        a=input("Какой вкус вы хотите добавить? ")
        flavor+=", "+a
        self.flavors=flavor
        print(f"обновлённые вкусы {self.flavors}")

    def remove_flavor(self, flavor):
        flavor=self.flavors
        a = input("Какой вкус закончился? ")
        flavor.remove(a)
        self.flavors = flavor
        print(f"обновлённые вкусы {self.flavors}")

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

ice_cream_stand = IceCreamStand("Морожняя", "Ice Cream", 4.3, ["Ванильный", "Шоколадный", "Клубничыный"], "СПб", "12  часов")
ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()
#ice_cream_stand = IceCreamStand("Морожняя", "Ice Cream", 4.3, "Ванильный", "СПб", "12  часов")
#ice_cream_stand.add_flavor()
ice_cream_stand.remove_flavor("Ванильный")




