def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):# свойства класса (характеристика объекта)
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):# метод класса describe_restaurant  выводит информацию о ресторане
           print (f"Название ресторана {self.restaurant_name}, кухня:{self.cuisine_type} итальянская.")#выводит информацию о ресторане
        def open_restaurant (self):# метод класса open_restaurant
            print ("Ресторан сейчас открыт.")# который выводит сообщение о том, что ресторан открыт
    newRestaurant = Restaurant ("Italiano"," ")#cоздаем объект newRestaurant класса Restaurant с аргументами "Italiano" и "".
    print (newRestaurant.restaurant_name)#вывод свойства restaurant_name объекта newRestaurant
    print (newRestaurant.cuisine_type)#Вывод свойства cuisine_type объекта newRestaurant

    newRestaurant.describe_restaurant()#вызываем методы
    newRestaurant.open_restaurant()
z1()
