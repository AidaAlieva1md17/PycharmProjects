number = int(input("Введите количество слов: "))
A = [0]*number
for i in range (0, number):
    print ("Введите слово: ")
    A[i] = input()
    i += 1
for i in range (0, number):
    print (A[i], end = ' ')
    i += 1