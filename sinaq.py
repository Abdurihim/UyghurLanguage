from PIL import Image, ImageDraw, ImageFont
from UyghurLanguageUtils import UyghurCharUtilities

text = 'يەنە بىر شەھەر'

text_to_be_reshaped = UyghurCharUtilities()
reshaped_text = text_to_be_reshaped.getUyPFStr(text, reverse=True)

font = ImageFont.truetype('./UKIJTuT.ttf', 55)

image = Image.new('RGBA', (800, 600), ('#fff'))
image_draw = ImageDraw.Draw(image)
image_draw.text((10,10), reshaped_text, fill=('#000'), font=font)

image.show()
