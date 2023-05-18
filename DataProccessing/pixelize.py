import numpy as np
from PIL import Image as im

class Pixelize:
    def __init__(self, height=720, width=1280):
        self.height = height
        self.width = width
        self.pixel_count = height * width
    
    def bitToPixel(self, fbits, target):
        fbytes = [255 * int(b) for b in fbits]
        array = np.array(fbytes).astype('uint8')
        reshaped_bytes = np.reshape(array, (self.height, self.width))
        data = im.fromarray(reshaped_bytes)
        data.save(target)
    
    def pixelToBit(self, target):
        pix = im.open(target)
        array = np.array(pix).flatten().tolist()
        bits = ""
        for a in array: bits += str(int(a) // 255)
        return bits
