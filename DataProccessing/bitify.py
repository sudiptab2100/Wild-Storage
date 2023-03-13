class Bitify:
    def __init__(self, ftype=0):
        self.ftype = ftype

    def fileToBits(self, target_dir):
        op = ""
        with open(target_dir, mode='rb') as file:
            fileContent = file.read()
            for fbyte in fileContent:
                op += bin(fbyte)[2:].zfill(8)
        return op

    def bitsToFile(self, fbits, target_dir):
        fbytes = bytes(int(fbits[i : i + 8], 2) for i in range(0, len(fbits), 8))
        with open(target_dir, mode='wb') as file:
            file.write(fbytes)
