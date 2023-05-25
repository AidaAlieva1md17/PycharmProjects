'Задание 4.1'
def number_by_3 (number:int):
    return True if number%3==0 else False
print ("Проверка функции деления на три")
print ( number_by_3(10))
print(number_by_3(9))
'Задание 4.2'
def number_by_100 (n):
    resultat= None
    try:
        resultat= 100/  float (n)
    except ValueError:
        print ('Нужно брать число!')
    except ZeroDivisionError:
        print('Ошибка: деление на ноль!')
    except  Exception as e:
        print ('Нельзя брать букву')
    return resultat
print ("Проверка функции деления на 100")
print (number_by_100(10))
print(number_by_100(0))
print(number_by_100("s"))
'Задание 4.3'
def magic_date(date: str):
    try:
        date = date.split(".")
        if int(date[0]) * int(date[1]) == int(date[2][2:]):
            return True
        else:
            return False
    except:
        print("Функция принимает строку с датой в формате dd.mm.yyyy")
print("Проверка функции магической даты")
print(magic_date("22.01.2022"))
print(magic_date("21.01.2022"))
'Задание 4.4'

def ticket(ticket: str):
    sum1 = sum([int(i) for i in ticket[:int(len(ticket) / 2)]])
    sum2 = sum([int(i) for i in ticket[int(len(ticket) / 2):]])
    if sum1 == sum2:
        return True
    else:
        return False
print("\nПроверка функции счастливого билета")
print(ticket("385916"))
print(ticket("231002"))