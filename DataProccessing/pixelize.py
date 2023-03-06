import numpy as np
from PIL import Image as im
from byted_file import *

class Pixelize:
    def __init__(self, height=720, width=1280):
        self.height = height
        self.width = width
        self.pixel_count = height * width

    def byteToPixel(self, bytedata, target):
        array = np.array(bytedata).astype('uint8')
        reshaped_bytes = np.reshape(array, (self.height, self.width))
        data = im.fromarray(reshaped_bytes)
        data.save(target)

    def pixelToByte(self, target):
        pix = im.open(target)
        return np.array(pix)
