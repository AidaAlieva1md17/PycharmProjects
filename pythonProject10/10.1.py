import json# продукты представлены как список словарей
# определяем функцию для вывода информации о продукте
def add_new_product(data):
  # запрашиваем новые данные у пользователя
    name = input('Введите название продукта: ')
    price = int(input('Введите цену продукта: '))
    weight = int(input('Введите вес продукта: '))
    available = input('В наличии? (Да/Нет): ').lower() == 'да'

    new_product = {
        'name': name,
        'price': price,
        'weight': weight,
        'available': available
    }
    print(data)# выводим словарь из  json
    data['products'].append(new_product)# добавляем  новый элемент в словарь  data  по ключу продукты, data products  список
    # записываем обновленные данные в файл
    with open('products.json', 'w') as json_file:
        json.dump(data, json_file)# превращения словаря в объект json и добавляет его в файл и сохраняет его
with open("products.json", "r", encoding='utf-8') as f: # открываем файл с данными о продуктах в режиме чтения с указанием кодировки
    data = json.load(f) # загружаем данные из json  файла
add_new_product(data) # добавляем продукты в объект словаря по ключу продукты
for product in data['products']: # цикл который проходится по всему списку  с обработкой
    print('Название: ' + product['name'])
    print('Цена: ' + str(product['price']))
    print('Вес: ' + str(product['weight']))
    if product['available']:
        print('В наличии')
    else:
        print('Нет в наличии')
