from PIL import Image, ImageFilter
import os

# создаем папку для сохранения новых изображений
if not os.path.exists("7.3 папка"):
    os.makedirs("7.3 папка")

# примененяем фильтр ко всем изображениям
for i in range(1, 6):
    # открытие изображения
    image = Image.open(f"{i}.jpg")

    # применяем фильтр резкости
    filt = image.filter(ImageFilter.SHARPEN)

    # сохраняем новое изображение
    filt.save(f"7.3 папка/{i}_filtered.jpg")