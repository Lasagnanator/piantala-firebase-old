# conversione di ogni tipo di immagine in jpg per mandarlo a plantnet

from PIL import Image
import os

# inserire path assoluto
IMAGE_PATH = '/Users/giuliolapovich/Code/aws-azure/piantala/img/IMG_1980.jpg'

# importing the image
im = Image.open(IMAGE_PATH)
print("The size of the image before conversion : ", end="")
print(os.path.getsize(IMAGE_PATH))

# converting to jpg
rgb_im = im.convert("RGB")

# ------------- facoltativo per stampa --------------------

# exporting the image
SAVED_IMAGE_PATH = '/Users/giuliolapovich/Code/aws-azure/piantala/img/IMG_1980_JPG.jpg'
rgb_im.save(SAVED_IMAGE_PATH)
print("The size of the image after conversion : ", end="")
print(os.path.getsize(SAVED_IMAGE_PATH))