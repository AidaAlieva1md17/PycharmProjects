from PIL import Image
image = Image.open("хомаа.jpg")
image.show()
width, height = image.size
print("Ширина:", width)
print("Высота:", height)
format = image.format
print("Формат:", format)
mode = image.mode
print("Цветовая модель:", mode)