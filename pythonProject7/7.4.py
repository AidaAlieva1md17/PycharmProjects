from PIL import Image, ImageDraw, ImageFont
import os
water= "image_watermark.png"
with Image.open(water) as img_water:
    img_water.load()
img_water = Image.open(water)
img_water = img_water.resize((img_water.width // 2, img_water.height // 2))


filename = "photo.jpg"
with Image.open(filename) as img:
    img.load()


img.paste(img_water, (42, 40), img_water)
img.save("watermark_photo.jpg")
