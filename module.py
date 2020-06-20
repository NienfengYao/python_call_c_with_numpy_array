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


def ex_np_array_3dim(lib):
	x = np.arange(24, dtype=np.float64).reshape((2,3,4))
	y = np.zeros_like(x)
	if not x.flags['C_CONTIGUOUS']:
		x = np.ascontiguous(x, dtype=x.dtype)

	func = lib.np_array_3dim
	_npp = ndpointer(dtype=np.float64, ndim=3, flags='C')
	func.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, _npp, _npp]
	func.restype = None
	m = ctypes.c_int(x.shape[0])
	n = ctypes.c_int(x.shape[1])
	o = ctypes.c_int(x.shape[2])
	func(m, n, o, x, y)
	print("x:", x)
	print("y:", y)


def ex_np_array_3dim_3ptr(lib):
	x = np.arange(24, dtype=np.float64).reshape((2,3,4))
	y = np.zeros_like(x)
	if not x.flags['C_CONTIGUOUS']:
		x = np.ascontiguous(x, dtype=x.dtype)

	# Init ctypes types
	DOUBLE = ctypes.c_double
	PDOUBLE = ctypes.POINTER(DOUBLE)
	PPDOUBLE = ctypes.POINTER(PDOUBLE)
	PPPDOUBLE = ctypes.POINTER(PPDOUBLE)

	# Init needed data types
	ARR_DIMX = DOUBLE*x.shape[2]
	ARR_DIMY = PDOUBLE*x.shape[1]
	ARR_DIMZ = PPDOUBLE*x.shape[0]

	# Init pointer
	x_arr_ptr = ARR_DIMZ()
	y_arr_ptr = ARR_DIMZ()

	# Fill the 2D ctypes array with values
	for i, row in enumerate(x):
		x_arr_ptr[i] = ARR_DIMY()
		y_arr_ptr[i] = ARR_DIMY()
		# print("arr_ptr[{}] = {}".format(i, arr_ptr[i]))
		for j, col in enumerate(row):
			x_arr_ptr[i][j] = ARR_DIMX()
			y_arr_ptr[i][j] = ARR_DIMX()
			# print("arr_ptr[{}][{}] = {}".format(i, j, arr_ptr[i][j]))
			for k, val in enumerate(col):
				x_arr_ptr[i][j][k] = val
				# print("arr_ptr[{}][{}][{}] = {}".format(i, j, k, arr_ptr[i][j][k]))


	func = lib.np_array_3dim_3ptr
	func.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, PPPDOUBLE, PPPDOUBLE]
	func.restype = None
	m = ctypes.c_int(x.shape[0])
	n = ctypes.c_int(x.shape[1])
	o = ctypes.c_int(x.shape[2])
	func(m, n, o, x_arr_ptr, y_arr_ptr)
	for i in range(2):
		for j in range(3):
			for k in range(4):
				y[i,j,k] = y_arr_ptr[i][j][k]
	print("x:", x)
	print("y:", y)


def ex_np_array_3dim_3ptr_xx(lib):
	x = np.arange(24, dtype=np.float64).reshape((2,3,4))
	y = np.zeros_like(x)
	if not x.flags['C_CONTIGUOUS']:
		x = np.ascontiguous(x, dtype=x.dtype)

	# Init ctypes types
	DOUBLE = ctypes.c_double
	PDOUBLE = ctypes.POINTER(DOUBLE)
	PPDOUBLE = ctypes.POINTER(PDOUBLE)
	PPPDOUBLE = ctypes.POINTER(PPDOUBLE)

	# Init needed data types
	ARR_DIMX = DOUBLE*x.shape[2]
	ARR_DIMY = PDOUBLE*x.shape[1]
	ARR_DIMZ = PPDOUBLE*x.shape[0]

	# Init pointer
	arr_ptr = ARR_DIMZ()

	# Fill the 2D ctypes array with values
	for i, row in enumerate(x):
		arr_ptr[i] = ARR_DIMY()
		for j, col in enumerate(row):
			arr_ptr[i][j] = ARR_DIMX()
			for k, val in enumerate(col):
				arr_ptr[i][j][k] = val


	func = lib.np_array_3dim_3ptr_xx
	# _npp = ndpointer(dtype=PPPDOUBLE, ndim=1, flags='C')
	func.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, PPPDOUBLE]
	func.restype = None
	m = ctypes.c_int(x.shape[0])
	n = ctypes.c_int(x.shape[1])
	o = ctypes.c_int(x.shape[2])
	func(m, n, o, arr_ptr)
	print("x:", x)


def main():
	lib = ctypes.cdll.LoadLibrary('./module.so')
	print('ex_int(): return the square of int')
	ex_square(lib)
	print('ex_np_array_1dim(): return y = x+1')
	ex_np_array_1dim(lib)
	print('ex_np_array_2dim(): return y = x+1')
	ex_np_array_2dim(lib)
	print('ex_np_array_3dim(): return y = x+1')
	ex_np_array_3dim(lib)
	print('ex_np_array_3dim_3ptr_xx()')
	ex_np_array_3dim_3ptr_xx(lib)
	print('ex_np_array_3dim_3ptr()')
	ex_np_array_3dim_3ptr(lib)


if __name__ == '__main__':
	main()
