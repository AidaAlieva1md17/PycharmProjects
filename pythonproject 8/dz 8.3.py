from  PIL import Image, ImageDraw

im = Image.open('postcarddr.jpg')
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (200,50),
    'masha   c dnem rojdenia',
    fill=('#1C0606')
    )
im.show()
