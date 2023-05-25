import json

def print_product_info(product):
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии")
    print()

with open("products.json", "r", encoding='utf-8') as f:
    data = json.load(f)

products = data["products"]

list(map(print_product_info, products))
import json

with open('products.json') as json_file:
    data = json.load(json_file)

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
data['products'].append(new_product)

with open('products.json', 'w') as json_file:
    json.dump(data, json_file)

for product in data['products']:
    print('Название: ' + product['name'])
    print('Цена: ' + str(product['price']))
    print('Вес: ' + str(product['weight']))
    if product['available']:
        print('В наличии')
    else:
        print('Нет в наличии')
    print()