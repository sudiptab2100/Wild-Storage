class BytedFile:
    def __init__(self, ftype=0):
        self.ftype = ftype

    def fileToBytes(self, target_dir):
        with open(target_dir, mode='rb') as file:
            fileContent = file.read()
            return fileContent
    
    def bytesToFile(self, fbytes, target_dir):
        with open(target_dir, mode='wb') as file:
            file.write(fbytes)

