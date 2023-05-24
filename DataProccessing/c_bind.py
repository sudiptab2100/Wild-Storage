from ctypes import *

c_lib = cdll.LoadLibrary('./DataProccessing/cLibs/c_lib.so')

def c_pixelToBit(array):
    size = len(array)
    carray = (c_int * size)(*array)

    c_lib.c_pixelToBit.argtypes = [POINTER(c_int), c_size_t]
    c_lib.c_pixelToBit.restype = c_char_p

    res = c_lib.c_pixelToBit(carray, size)
    return res.decode('utf-8')

def c_expandSlab(slab, exp, width):
	cslab = c_char_p(slab.encode('utf-8'))
	c_lib.c_expandSlab.argtypes = [c_char_p, c_int, c_int]
	c_lib.c_expandSlab.restype = c_char_p

	res = c_lib.c_expandSlab(cslab, exp, width)
	return res.decode('utf-8')

def c_compressSlab(slab, exp, width, pixel_count):
    cslab = c_char_p(slab.encode('utf-8'))
    c_lib.c_compressSlab.argtypes = [c_char_p, c_int, c_int, c_int]
    c_lib.c_compressSlab.restype = c_char_p

    res = c_lib.c_compressSlab(cslab, exp, width, pixel_count)
    return res.decode('utf-8')