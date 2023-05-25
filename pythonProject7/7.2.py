from PIL import Image
filename = ("хома3.jpg")
with Image.open(filename) as img:
    img.load()
# image = Image.open("хомаа.jpg")

# уменьшаем изображение в три раза
width, height = img.size
new_img =img.resize((img.width // 3, img.height // 3))

# получаем зеркальные образцы изображения
hom_lr = img.transpose(Image.FLIP_LEFT_RIGHT)
hom_tb = img.transpose(Image.FLIP_TOP_BOTTOM)

# сохраняем
new_img.save("хома2.jpg")
hom_lr.save("хома4.jpg")
hom_tb.save("хома5.jpg")