import cv2
import numpy as np
from PIL import Image, ImageFilter

img1 = Image.open("girl.jpeg")
img2 = Image.open("face0.jpg")

img1.paste(img2, (400, 72))
img1.show()
