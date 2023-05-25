class IceCreamStand:#создание класса "IceCreamStand"
    def __init__(self, name, flavors):#определение класса с параметрами "name" и "flavors"
        self.name = name#определение класса с параметрами "name" и "flavors"
        self.flavors = flavors #cоздание атрибута "flavors" для объекта класса

    def display_flavors(self):#определение метода "display_flavors" для объектов класса
        for flavor in self.flavors:#цикл по всем элементам списка "flavors"
            print(flavor) #вывод текущего элемента списка на экран


my_ice_cream_stand = IceCreamStand("Мороженное", ["Ванильный", "Шоколадный", "Клубничный"])#создание объекта класса "IceCreamStand" с параметрами "мороженное" и списком ванильный итд

import tkinter as tk #импортирование все из библиотеки tkinter под сокращение "tk"

root = tk.Tk()#активация конструктора. Новое окно присваивается переменной root
root.title("Вкусы мороженного")#пишем заголовок  для окна

name_label = tk.Label(root, text=my_ice_cream_stand.name)# создание окошка Label( показывает текст либо изображени) с текстом из атрибута "name" объекта "my_ice_cream_stand"
name_label.pack()#вывод "name_label" в окно

flavors_label = tk.Label(root, text="Вкусы мороженного:")#создание базового блока графического интерфейса Label с текстом вкус мороженного
flavors_label.pack()# вывод блокавкус мороженного в окно

flavors_listbox = tk.Listbox(root)# создание прямоугольного блока графического интерфейса Listbox
for flavor in my_ice_cream_stand.flavors:#цикл по всем элементам списка "flavors" объекта "my_ice_cream_stand"
    flavors_listbox.insert(tk.END, flavor)# добавление текущего элемента списка в блок  "flavors_listbox"
flavors_listbox.pack()#вывод "flavors_listbox" в окно

root.mainloop()#запуск бесконечного цикла