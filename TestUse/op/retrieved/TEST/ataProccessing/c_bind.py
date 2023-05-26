from ctypes import *
import os.path

c_lib = cdll.LoadLibrary(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "cLibs/c_lib.so")

def c_pixelToBit(pix):
    height, width = pix.shape
    data_ptr = pix.ctypes.data_as(POINTER(c_uint8))
    c_lib.c_pixelToBit.restype = c_char_p
    res = c_lib.c_pixelToBit(data_ptr, height, width)
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