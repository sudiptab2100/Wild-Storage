from pixelize import Pixelize
import json

class FrameGenerator:
    def __init__(self, height=720, width=1280):
        self.height = height
        self.width = width
        self.pixel_count = height * width
        self.p = Pixelize(height=self.height, width=self.width)

    def __bitSlabs(self, bitdata, n):
        for i in range(0, n, self.pixel_count):
            yield bitdata[i: i + self.pixel_count]
    
    def __padSize(self, bitdata, n):
        ext = n % self.pixel_count

        if ext != 0: return (self.pixel_count - ext)
        return 0

    def storeFrames(self, bitdata, target_dir):
        i = 0
        noOfBytes = len(bitdata)
        pads = self.__padSize(bitdata, noOfBytes)
        bitdata += "0" * pads
        slabs = self.__bitSlabs(bitdata, noOfBytes + pads)
        for slab in slabs:
            self.p.bitToPixel(slab, f"{target_dir}{i}.png")
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

    def framesToBits(self, target_dir):
        metadata = ''
        with open(f"{target_dir}metadata.json", "r") as f:
            metadata = json.load(f)
        
        n = metadata['frames']
        bitdata = ""
        for i in range(n):
            bitdata += self.p.pixelToBit(f"{target_dir}{i}.png")

        return bitdata[: metadata['bytes']]
