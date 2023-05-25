from  PIL import Image
d= {1:"postcarddr.jpg", 2:"postcardnewyear.jpg",3:"postcard8marta.jpg" }
print ("1 - День родения\n"
"2- Новый год\n"
"3- 8 марта")
ans = int (input ("Для получения открытки введите число - номер праздника:"))
filename= d[ans]
with Image.open (filename) as img:
    img.load()
img.show()