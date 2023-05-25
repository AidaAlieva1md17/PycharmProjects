import os
def prog1():
    import os # используем функции создание папки, просмотр файлов в папке
    from PIL import Image, ImageFilter
    print("Мероприятие: \n"
          "1.Детализировать\n"
          "2.Улучшить резкость\n"
          "3.Найти контуры\n"
          "4.Тисневое изоб\n")# наше меню
    a=int(input())# ввод пользователя
    current_dir = os.getcwd()# текущую папку занесли в переменную папку
    directory=os.listdir((current_dir)+"\до")# показывает содержимое папки os.getcwd- путь текущая директория и изображение папки
    print(directory)# вывод содержимого в папке на экран
    eff = [ImageFilter.DETAIL, ImageFilter.SHARPEN, ImageFilter.CONTOUR,ImageFilter.EMBOSS]# создаем фильтр
    for file in directory:# проходимся по каждому файлу в папке# меняем текущую папку с помощью  chande dir
        os.chdir(current_dir + "\до")
        with Image.open(file) as img:# открываем файл как картинку
            os.chdir(current_dir+"\после")# меняем текущую папку с помощью  chande dir  getcwd  показывает текущую папку
            img.load()#загружаем картинку
            new_img = img.filter(eff[a - 1])#применяем фильтр. берем фильр из списка  по индексу а-1( индексация списков начинается с нуля)
            new_img.save(file)

current_dir = os.getcwd()
def prog2():
    import os
    from PIL import Image, ImageFilter
    print("Мероприятие: \n"
          "1.Детализировать\n"
          "2.Улучшить резкость\n"
          "3.Найти контуры\n"
          "4.Тисневое изоб\n")
    a = int(input())
    directory = os.listdir(current_dir + "\до")
    eff = [ImageFilter.DETAIL, ImageFilter.SHARPEN, ImageFilter.CONTOUR, ImageFilter.EMBOSS]
    for file in directory:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif',
                                  '.bmp')):# проверка расширения через формат endswith   смотрим на что заканчивается строка
         print (file)
         os.chdir( current_dir+'\до')
         with Image.open(file) as img:
                os.chdir( current_dir+'\после')
                img.load()
                new_img = img.filter(eff[a - 1])
                new_img.save(file)
def prog3():
    import csv  #формат файлов где данные между собой ;  библиотека которая читает эти файлы
    a=0
    with open("data.csv", newline='') as file:# читаем этот файл, открываем его
        r=csv.DictReader(file,delimiter=",")# передаем его в csv передает значения как словарь и разделяется запятой
        for i in r:# проходимся по списку r который содержит элементы в виде словарей
            print (f'{i["Продукт"]} {i["Количество"]} шт. за {(i["Цена"])}' )
            a+=int(i["Количество"])* int(i["Цена"])
    print(a)
prog3()
prog1()
