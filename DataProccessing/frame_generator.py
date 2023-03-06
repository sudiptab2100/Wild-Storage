from pixelize import Pixelize
import json

class FrameGenerator:
    def __init__(self, height=720, width=1280):
        self.height = height
        self.width = width
        self.pixel_count = height * width
        self.p = Pixelize(height=self.height, width=self.width)

    def __byteSlabs(self, bytedata, n):
        for i in range(0, n, self.pixel_count):
            yield bytedata[i: i + self.pixel_count]
    
    def __padSize(self, bytedata, n):
        ext = n % self.pixel_count

        if ext != 0: return (self.pixel_count - ext)
        return 0

    def storeFrames(self, bytedata, target_dir):
        i = 0
        noOfBytes = len(bytedata)
        pads = self.__padSize(bytedata, noOfBytes)
        bytedata.extend([0] * pads)
        slabs = self.__byteSlabs(bytedata, noOfBytes + pads)
        for slab in slabs:
            self.p.byteToPixel(slab, f"{target_dir}{i}.png")
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

    def framesToByte(self, target_dir):
        metadata = ''
        with open(f"{target_dir}metadata.json", "r") as f:
            metadata = json.load(f)
        
        n = metadata['frames']
        bytedata = []
        for i in range(n):
            bytedata += self.p.pixelToByte(f"{target_dir}{i}.png")

        return bytedata[: metadata['bytes']]
