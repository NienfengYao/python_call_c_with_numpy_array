import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer


"""
* ndpointer: 
  An ndpointer instance is used to describe an ndarray in restypes and argtypes specifications.
"""
def ex_square(lib):
	square = lib.square
	print(square(5))


def ex_np_array_1dim(lib):
	x = np.arange(0,10,dtype=np.float64)
	y = np.zeros(10, dtype=np.float64)
	dim1 = lib.np_array_1dim
	dim1.restype = None
	dim1.argtypes = [ndpointer(ctypes.c_double),
		ctypes.c_size_t,
		ndpointer(ctypes.c_double)]
	dim1(x, x.size, y)
	print("x:", x)
	print("y:", y)


def main():
	lib = ctypes.cdll.LoadLibrary('./module.so')
	print('ex_int(): return the square of int')
	ex_square(lib)
	print('ex_np_array_1dim(): return y = x+1')
	ex_np_array_1dim(lib)


if __name__ == '__main__':
	main()
