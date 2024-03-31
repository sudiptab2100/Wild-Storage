from DataProccessing.pixelize import Pixelize
import json
from collections import Counter
from DataProccessing.c_bind import c_expandSlab, c_compressSlab
from joblib import Parallel, delayed

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
    
    def getPixOnce(self, idx, slab):
        ext_slab = self.__expandSlab(slab)
        pix = self.p.bitToPixel(ext_slab)
        return idx, pix
    
    def storeFrames(self, bitdata, target_dir):
        noOfBytes = len(bitdata)
        pads = self.__padSize(bitdata, noOfBytes)
        bitdata += "0" * pads
        slabs = self.__bitSlabs(bitdata, noOfBytes + pads)
        img_arr = Parallel(n_jobs=-1)(delayed(self.getPixOnce)(i, slab) for i, slab in enumerate(slabs))
        img_arr = [x[1] for x in sorted(img_arr, key=lambda x: x[0])]
        
        metadata = dict()
        metadata['bytes'] = noOfBytes
        metadata['pad_size'] = pads
        metadata['frames'] = len(img_arr)
        metadata['height'] = self.height
        metadata['width'] = self.width
        metadata['pixel_count'] = self.pixel_count

        with open(f"{target_dir}metadata.json", "w") as outfile:
            json.dump(metadata, outfile, indent=4)
        
        return img_arr
    
    def getBitsOnce(self, idx, pix):
        ext_slab = self.p.pixelToBit(pix)
        bit_slab = self.__compressSlab(ext_slab)
        return idx, bit_slab
    
    def framesToBits(self, target_dir, img_arr):
        metadata = ''
        with open(f"{target_dir}metadata.json", "r") as f:
            metadata = json.load(f)
        
        n = metadata['frames']
        bit_slabs = Parallel(n_jobs=-1)(delayed(self.getBitsOnce)(i, img_arr[i]) for i in range(n))
        bit_slabs = [x[1] for x in sorted(bit_slabs, key=lambda x: x[0])]
        bitdata = "".join(bit_slabs)

        return bitdata[: metadata['bytes']]
