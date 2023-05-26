import cv2
import json

class FrameVideo:
    def __init__(self, ftype=0):
        self.ftype = ftype
    
    def __getMetadata(self, target_dir):
        with open(f"{target_dir}metadata.json", "r") as f:
            return json.load(f)
    
    def __frames(self, img_arr, n):
        for i in range(n):
            fi_path = f"{target_dir}{i}.png"
            yield cv2.imread(fi_path, cv2.IMREAD_GRAYSCALE)
    
    def framesToVideo(self, target_dir, img_arr):
        metadata = self.__getMetadata(target_dir)
        n = metadata['frames']
        out = cv2.VideoWriter(target_dir + 'op.mp4', cv2.VideoWriter_fourcc(*'MPNG'), 24, (metadata['width'], metadata['height']), 0)
        for frame in img_arr:
            out.write(frame)
        out.release()

    def extractFrames(self, target):
        metadata = self.__getMetadata(target)
        vidObj = cv2.VideoCapture(target + 'op.mp4')

        img_arr = []
        success = True
        while success:
            success, image = vidObj.read()

            if success: 
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                img_arr.append(image)
        
        return img_arr

    def test(self, target):
        f = self.__frames(target, 1)
        for _ in f:
            print(type(_))
            print(_.dtype)
            print(_.ndim)
            print(_[67])
            print(_.shape)