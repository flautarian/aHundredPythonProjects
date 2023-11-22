# text Watermark

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import matplotlib.pyplot as plt

script_dir = os.path.dirname(__file__)

image = Image.open(f"{script_dir}/puppy.png")
 
# this open the photo viewer
image.show() 
plt.imshow(image)

watermark_image = image.copy()
 
draw = ImageDraw.Draw(watermark_image)
 
w, h = image.size
x, y = int(w / 2), int(h / 2)
if x > y:
  font_size = y
elif y > x:
  font_size = x
else:
  font_size = x
   
font = ImageFont.truetype("arial.ttf", int(font_size/6))
 
# add watermark
draw.text((x, y), "puppy", fill=(0, 0, 0), font=font, anchor='ms')
plt.subplot(1, 2, 1)
plt.title("black text")
plt.imshow(watermark_image)
watermark_image.save(f"{script_dir}/puppy-black", format="PNG")
 
# add watermark
draw.text((x, y), "puppy", fill=(255, 255, 255), font=font, anchor='ms')
plt.subplot(1, 2, 2)
plt.title("white text")
plt.imshow(watermark_image)
