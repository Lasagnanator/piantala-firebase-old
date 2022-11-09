import PIL.Image
from pprint import pprint

IMAGE_PATH = '/Users/giuliolapovich/Code/aws-azure/piantala/img/IMG_1980.jpg'

img = PIL.Image.open(IMAGE_PATH)
exif_data = img._getexif()

# esporta json con i metadati dell'immagine
pprint(exif_data)
