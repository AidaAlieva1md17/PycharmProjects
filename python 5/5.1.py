spicok=[1,2,3,4,5]
n=0
chiclo= int(input('Введите число:'))
for i in range(5):
    if chiclo== spicok[i]:
        n+=4
if n>0:
    print (spicok)
    print ('Вы угадали число!')
else:
    print('Нет такого числа!')
