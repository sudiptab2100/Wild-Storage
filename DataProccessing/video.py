import cv2
import json

class FrameVideo:
    def __init__(self, ftype=0):
        self.ftype = ftype
    
    def __getMetadata(self, target_dir):
        with open(f"{target_dir}metadata.json", "r") as f:
            return json.load(f)
    
    def __frames(self, target_dir, n):
        for i in range(n):
            fi_path = f"{target_dir}{i}.png"
            yield cv2.imread(fi_path, cv2.IMREAD_GRAYSCALE)
    
    def framesToVideo(self, target_dir, dest):
        metadata = self.__getMetadata(target_dir)
        n = metadata['frames']
        out = cv2.VideoWriter(dest + 'op.mp4', cv2.VideoWriter_fourcc(*'MPNG'), 10, (metadata['width'], metadata['height']), 0)
        for frame in self.__frames(target_dir, n):
            out.write(frame)
        out.release()

    def extractFrames(self, target, dest):
        metadata = self.__getMetadata(target)
        vidObj = cv2.VideoCapture(target + 'op.mp4')
    
        count = 0
        success = True
        while success:
            success, image = vidObj.read()

            if success: 
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(f"{dest}{count}.png", image)
                count += 1
