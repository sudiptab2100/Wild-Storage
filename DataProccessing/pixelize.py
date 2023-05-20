import numpy as np
from PIL import Image as im

class Pixelize:
    def __init__(self, height=720, width=1280):
        self.height = height
        self.width = width
        self.pixel_count = height * width
    
    def bitToPixel(self, fbits):
        fbytes = [255 * int(b) for b in fbits]
        array = np.array(fbytes).astype('uint8')
        pix = np.reshape(array, (self.height, self.width))
        return pix
    
    def pixelToBit(self, pix):
        array = np.array(pix).flatten().tolist()
        bits = ''.join([str(int(int(a) / 255 > 0.5)) for a in array])
        return bits
