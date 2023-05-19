class Bitify:
    def __init__(self, ftype=0):
        self.ftype = ftype

    def fileToBits(self, target_dir):
        with open(target_dir, 'rb') as file:
            binary_data = file.read()
        binary_string = ''.join(format(byte, '08b') for byte in binary_data)
        return binary_string

    def bitsToFile(self, fbits, target_dir):
        fbytes = bytes(int(fbits[i : i + 8], 2) for i in range(0, len(fbits), 8))
        with open(target_dir, mode='wb') as file:
            file.write(fbytes)
