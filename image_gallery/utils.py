from PIL import Image

def compressImage(imagePath):
    image = Image.open(imagePath)
    image.save(imagePath,  format=image.format, quality=70)