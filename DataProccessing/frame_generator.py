from pixelize import Pixelize
import json
from collections import Counter
from c_bind import c_expandSlab, c_compressSlab

class FrameGenerator:
    def __init__(self, height=720, width=1280, exp=1):
        self.height = height
        self.width = width
        self.pixel_count = height * width
        self.p = Pixelize(height=self.height, width=self.width)
        self.exp = exp

    def __bitSlabs(self, bitdata, n):
        chunk_size = self.pixel_count // (self.exp ** 2)
        for i in range(0, n, chunk_size):
            yield bitdata[i: i + chunk_size]
    
    def __padSize(self, bitdata, n):
        chunk_size = self.pixel_count // (self.exp ** 2)
        ext = n % chunk_size

        if ext != 0: return (chunk_size - ext)
        return 0

    def __expandSlab(self, slab):
        return c_expandSlab(slab, self.exp, self.width)
    
    def __compressSlab(self, slab):
        return c_compressSlab(slab, self.exp, self.width, self.pixel_count)
    
    # For testing expansion and compression
    # def test(self, bitdata):
    #     e = self.__expandSlab(bitdata)
    #     e = e[: 3] + '1' + e[4:]
    #     c = self.__compressSlab(e)
    #     print()
    #     for i in range(0, len(e), self.width):
    #         print(*e[i: i + self.width])
    #     print()
    #     for i in range(0, len(c), self.width // self.exp):
    #         print(*c[i: i + self.width // self.exp])

    def storeFrames(self, bitdata, target_dir):
        i = 0
        noOfBytes = len(bitdata)
        pads = self.__padSize(bitdata, noOfBytes)
        bitdata += "0" * pads
        slabs = self.__bitSlabs(bitdata, noOfBytes + pads)
        img_arr = []
        for slab in slabs:
            ext_slab = self.__expandSlab(slab)
            pix = self.p.bitToPixel(ext_slab)
            img_arr.append(pix)
            i += 1
        
        metadata = dict()
        metadata['bytes'] = noOfBytes
        metadata['pad_size'] = pads
        metadata['frames'] = i
        metadata['height'] = self.height
        metadata['width'] = self.width
        metadata['pixel_count'] = self.pixel_count

        with open(f"{target_dir}metadata.json", "w") as outfile:
            json.dump(metadata, outfile)
        
        return img_arr

    def framesToBits(self, target_dir, img_arr):
        metadata = ''
        with open(f"{target_dir}metadata.json", "r") as f:
            metadata = json.load(f)
        
        n = metadata['frames']
        bitdata = ''.join([self.__compressSlab(self.p.pixelToBit(img_arr[i])) for i in range(n)])

        return bitdata[: metadata['bytes']]
