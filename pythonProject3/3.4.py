from random import randint

nepravilno = 0
pravilno = 0
while nepravilno != 3:
    a = randint(1, 100)
    b = randint(1, 100)
    summ = a + b
    print(a, "+", b)
    res = int(input())
    if res == summ:
        print("Правильно")
        pravilno += 1
    else:
        nepravilno += 1
        print("Ответ неправильный")
print("Игра окончена", "Правильных ответов", pravilno)