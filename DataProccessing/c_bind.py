from ctypes import *

c_lib = cdll.LoadLibrary('./DataProccessing/cLibs/c_lib.so')

def c_pixelToBit(array):
    size = len(array)
    carray = (c_int * size)(*array)

    c_lib.c_pixelToBit.argtypes = [POINTER(c_int), c_size_t]
    c_lib.c_pixelToBit.restype = c_char_p

    res = c_lib.c_pixelToBit(carray, size)
    return res.decode('utf-8')