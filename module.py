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
	y = np.zeros_like(x)
	dim1 = lib.np_array_1dim
	dim1.restype = None
	dim1.argtypes = [ndpointer(ctypes.c_double),
		ctypes.c_size_t,
		ndpointer(ctypes.c_double)]
	dim1(x, x.size, y)
	print("x:", x)
	print("y:", y)


def ex_np_array_2dim(lib):
	"""
    * np.uintp(Numpy type) = uintptr_t(C type). Integer large enough to hold a pointer.
    * ndpointer: Array-checking restype/argtypes
	"""
	x = np.arange(9, dtype=np.float64).reshape((3,3))
	y = np.zeros_like(x)
	_doublepp = ndpointer(dtype=np.uintp, ndim=1, flags='C')
	# _doublepp = ndpointer(dtype=np.uintp, ndim=2, flags='C') # error
	dim2 = lib.np_array_2dim
	dim2.argtypes = [ctypes.c_int, ctypes.c_int, _doublepp, _doublepp]
	dim2.restype = None
	# print(x.shape, x.shape[0], x.strides, x.strides[0])
	xpp = (x.__array_interface__['data'][0] + np.arange(x.shape[0])*x.strides[0]).astype(np.uintp)
	# print(x.__array_interface__['data'][0],  np.arange(x.shape[0]), x.strides[0])
	# print(xpp)
	ypp = (y.__array_interface__['data'][0] + np.arange(y.shape[0])*y.strides[0]).astype(np.uintp) 
	# print(y.__array_interface__['data'][0],  np.arange(y.shape[0]), y.strides[0])
	# print(ypp)
	m = ctypes.c_int(x.shape[0])
	n = ctypes.c_int(x.shape[1])
	dim2(m, n, xpp, ypp)
	print("x:", x)
	print("y:", y)


def main():
	lib = ctypes.cdll.LoadLibrary('./module.so')
	print('ex_int(): return the square of int')
	ex_square(lib)
	print('ex_np_array_1dim(): return y = x+1')
	ex_np_array_1dim(lib)
	print('ex_np_array_2dim(): return y = x+1')
	ex_np_array_2dim(lib)


if __name__ == '__main__':
	main()
